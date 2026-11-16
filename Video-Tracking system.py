from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QCheckBox, QMessageBox, QRubberBand, QPushButton, QLineEdit
from PyQt5.QtCore import QPoint, QRect, QSize, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QPixmap, QImage
from pathlib import Path
from picamera2 import Picamera2
import numpy as np
import config
import datetime
import cv2
import os

# Fuerza XCB para compatibilidad con Wayland en Raspberry Pi 5
os.environ["QT_QPA_PLATFORM"] = "xcb"

# Ruta para la carpeta output directamente en el Escritorio del usuario
DESKTOP_OUTPUT_DIR = Path.home() / "Desktop" / "output_tracking"

# Hilo para lectura fluida del sensor IMX477
class CameraThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    error_signal = pyqtSignal(str)

    def __init__(self, camera_index):
        super().__init__()
        self.camera_index = camera_index
        self._run_flag = True
        self.picam2 = None

    def run(self):
        try:
            self.picam2 = Picamera2(self.camera_index)
            video_config = self.picam2.create_video_configuration(
                main={"size": (config.WIDTH_IMAGE, config.HEIGHT_IMAGE), "format": "RGB888"}
            )
            self.picam2.configure(video_config)
            self.picam2.start()

            while self._run_flag:
                frame = self.picam2.capture_array()
                cv_img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                self.change_pixmap_signal.emit(cv_img)
                self.msleep(15)

        except Exception as e:
            self.error_signal.emit(f"Error al iniciar Cámara {self.camera_index}: {str(e)}")
        finally:
            if self.picam2:
                try:
                    self.picam2.stop()
                    self.picam2.close()
                except:
                    pass

    def stop(self):
        self._run_flag = False
        self.wait()


class CameraTrackerWindow(QWidget):
    def __init__(self, cam_index):
        super().__init__()
        self.cam_index = cam_index
        self.thread = None
        self.current_frame = None
        
        # Incremento de tamaño en la ventana
        self.window_width = config.WIDTH_IMAGE + 100
        self.header_height = 70
        self.window_height = config.HEIGHT_IMAGE + self.header_height + 50
        
        self.total = 0    
        self.minSize = 10
        
        self.resize(self.window_width, self.window_height)
        self.setWindowTitle(f'Cámara {self.cam_index}')

        self.connectedCamera = False
        self.visibleObject = False
        self.is_tracking = False

        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.origin = QPoint()
        self.final = QPoint()
        
        self.posX = 0
        self.posY = 0
        self.radiusX = 0
        self.radiusY = 0
        
        self.fileData = None
        self.out = None
        self.timestamp = None
        self.time = None

        self.initUI()

    def initUI(self):
        # Fila 1: Opciones y botones de control
        self.cb = QCheckBox('Auto Exp', self)
        self.cb.move(10, 8)
        self.cb.setFont(QFont("Arial", 8))
        
        self.saveVideo = QCheckBox('Save video', self)
        self.saveVideo.move(10, 26)
        self.saveVideo.setFont(QFont("Arial", 8))

        self.startButton = QPushButton(f"Start Cam {self.cam_index}", self)
        self.startButton.clicked.connect(self.clickStartVideo)
        self.startButton.move(100, 8)
        self.startButton.resize(95, 28)
        self.startButton.setFont(QFont("Arial", 8))

        self.snsButton = QPushButton("Snapshot", self)
        self.snsButton.clicked.connect(self.clickSaveSns)
        self.snsButton.move(200, 8)
        self.snsButton.resize(75, 28)
        self.snsButton.setFont(QFont("Arial", 8))
        self.snsButton.setEnabled(False)

        self.Trackboton = QPushButton("Tracking", self)
        self.Trackboton.clicked.connect(self.clickTracking)
        self.Trackboton.move(280, 8)  
        self.Trackboton.resize(75, 28)
        self.Trackboton.setFont(QFont("Arial", 8))
        self.Trackboton.setEnabled(False)

        self.stopButton = QPushButton("Stop", self)
        self.stopButton.clicked.connect(self.clickStopTracking)
        self.stopButton.move(360, 8)
        self.stopButton.resize(55, 28)
        self.stopButton.setFont(QFont("Arial", 8))
        self.stopButton.setEnabled(False)

        # Fila 2: Monitor de valores ubicado justo debajo de los botones principales
        self.lblLiveVals = QLabel("X: -   |   Y: -   |   W: -   |   H: -", self)
        self.lblLiveVals.move(100, 42)
        self.lblLiveVals.resize(self.window_width - 110, 22)
        self.lblLiveVals.setFont(QFont("Arial", 10, QFont.Bold))

        # Visualizador del video
        self.label = QLabel(self)
        self.label.setScaledContents(True)
        self.label.move(0, self.header_height)
        self.label.resize(self.window_width, self.window_height - self.header_height)

    def clickStartVideo(self):
        if self.thread is None:
            self.thread = CameraThread(self.cam_index)
            self.thread.change_pixmap_signal.connect(self.update_image)
            self.thread.error_signal.connect(self.handle_error)
            self.thread.start()
            self.connectedCamera = True
            self.startButton.setEnabled(False)

    def handle_error(self, err_msg):
        QMessageBox.warning(self, "Error de Cámara", err_msg, QMessageBox.Ok)
        self.startButton.setEnabled(True)
        if self.thread:
            self.thread.stop()
            self.thread = None

    def update_image(self, cv_img):
        self.current_frame = cv_img.copy()
        self.total += 1
        
        if self.visibleObject or self.is_tracking:
            cv_img = self.tracking(cv_img)
            
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        convert_to_Qt_format = QImage(rgb_image.data, w, h, ch * w, QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(convert_to_Qt_format))

    def clickSaveSns(self):
        if self.current_frame is not None:
            folder = DESKTOP_OUTPUT_DIR / f'Cam_{self.cam_index}_{self.timestamp}' / 'snapshots'
            folder.mkdir(parents=True, exist_ok=True)
            cv2.imwrite(str(folder / f'{self.time.replace(":", "-")}.png'), self.current_frame)

    def clickTracking(self):
        self.setWindowTitle(f'Cámara {self.cam_index} - [TRACKING ACTIVO]')
        if self.fileData is None:
            now = datetime.datetime.now()
            self.timestamp = str(now.strftime('%Y%m%d_%H-%M-%S'))
            folder = DESKTOP_OUTPUT_DIR / f'Cam_{self.cam_index}_{self.timestamp}'
            folder.mkdir(parents=True, exist_ok=True)
            
            self.fileData = open(folder / 'tracking.txt', 'w')
            self.fileData.write('time, frame_num, center_X_px, center_Y_px, width_px, height_px\n')
            
        self.is_tracking = True
        self.total = 0
        self.Trackboton.setEnabled(False)
        self.stopButton.setEnabled(True)
        self.snsButton.setEnabled(True)

    def clickStopTracking(self):  
        self.setWindowTitle(f'Cámara {self.cam_index}')
        if self.fileData:
            self.fileData.close()
            self.fileData = None
        self.is_tracking = False
        self.visibleObject = False
        self.Trackboton.setEnabled(False)
        self.stopButton.setEnabled(False)
        self.snsButton.setEnabled(False)
        self.lblLiveVals.setText("X: -   |   Y: -   |   W: -   |   H: -")
        
        if self.out:
            self.out.release()
            self.out = None
        QMessageBox.information(self, 'Tracking', f'Tracking detenido en Cámara {self.cam_index}', QMessageBox.Ok)

    def mousePressEvent(self, event):  
        if self.connectedCamera and not self.is_tracking:    
            self.origin = QPoint(event.pos())
            self.rubberBand.setGeometry(QRect(self.origin, QSize()))
            self.rubberBand.show()

    def mouseMoveEvent(self, event):
        if self.connectedCamera and not self.is_tracking:
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())
    
    def mouseReleaseEvent(self, event):
        if self.connectedCamera and not self.is_tracking:
            self.final = QPoint(event.pos())
            w_sel = abs(self.final.x() - self.origin.x())
            h_sel = abs(self.final.y() - self.origin.y())
            
            if w_sel <= self.minSize or h_sel <= self.minSize:
                self.rubberBand.hide()
                self.visibleObject = False
                self.Trackboton.setEnabled(False)
            else:
                x_start = min(self.origin.x(), self.final.x())
                y_start = min(self.origin.y(), self.final.y())
                
                self.posX = x_start
                self.posY = max(0, y_start - self.header_height)
                self.radiusX = w_sel // 2
                self.radiusY = h_sel // 2
                
                self.visibleObject = True        
                self.Trackboton.setEnabled(True)
                self.rubberBand.hide()

    def tracking(self, img):
        # Formato en segundos exactos (HH:MM:SS)
        self.time = datetime.datetime.now().strftime('%H:%M:%S')
        self.image = img.copy()

        borderX, borderY = self.radiusX, self.radiusY
        ay = max(0, self.posY - borderY)
        by = min(self.image.shape[0], self.posY + self.radiusY * 2 + borderY)
        ax = max(0, self.posX - borderX)
        bx = min(self.image.shape[1], self.posX + self.radiusX * 2 + borderX)

        frameRoi = self.image[ay:by, ax:bx]

        if frameRoi.size > 0 and self.is_tracking:
            frameRoiGray = cv2.cvtColor(frameRoi, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(frameRoiGray, (5, 5), 0)
            _, dst = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            bwimage = cv2.bitwise_not(dst)

            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
            bwimage = cv2.morphologyEx(bwimage, cv2.MORPH_OPEN, kernel)

            cX, cY, cW, cH = cv2.boundingRect(bwimage)
            if cW > 0 and cH > 0:
                self.posX = max(0, self.posX - borderX) + cX
                self.posY = max(0, self.posY - borderY) + cY
                self.radiusX, self.radiusY = cW // 2, cH // 2

        centerX = self.posX + self.radiusX
        centerY = self.posY + self.radiusY
        width_px = self.radiusX * 2
        height_px = self.radiusY * 2

        # 1. Cuadro visualizador y punto central
        cv2.rectangle(self.image, (self.posX, self.posY), (self.posX + width_px, self.posY + height_px), (0, 0, 255), 2)
        cv2.circle(self.image, (int(centerX), int(centerY)), 3, (0, 255, 0), -1)

        # 2. Monitor visual en tiempo real
        self.lblLiveVals.setText(f"X: {centerX}   |   Y: {centerY}   |   W: {width_px}   |   H: {height_px}")

        # 3. Guardado en archivo .txt
        if self.is_tracking and self.fileData:
            log_line = f"{self.time}, {self.total}, {centerX}, {centerY}, {width_px}, {height_px}\n"
            self.fileData.write(log_line)

        # Grabación de video si está activa
        if self.is_tracking and self.saveVideo.isChecked():
            folder = DESKTOP_OUTPUT_DIR / f'Cam_{self.cam_index}_{self.timestamp}'
            if self.out is None:
                self.out = cv2.VideoWriter(str(folder / 'video.mp4'), cv2.VideoWriter_fourcc(*'mp4v'), config.FPS_VIDEO_SHOW, (self.image.shape[1], self.image.shape[0]))
            self.out.write(self.image)

        return self.image

    def closeEvent(self, event):
        if self.thread is not None:
            self.thread.stop()
        if self.fileData:
            self.fileData.close()
        if self.out:
            self.out.release()


if __name__ == '__main__':
    # Crear automáticamente la carpeta output_tracking en el Escritorio
    DESKTOP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    app = QApplication([])

    win1 = CameraTrackerWindow(cam_index=0)
    win1.move(30, 60)
    win1.show()

    win2 = CameraTrackerWindow(cam_index=1)
    win2.move(700, 60)
    win2.show()

    app.exit(app.exec_())