#proyecto Final Gracida Salgado Angel David#
from vpython import *
from random import random,randint
N=int(input("dame el numero atomico"))
n=150
T=2*pi/n
a=2*pi
ro=5.0
a1=a2=0.0


for i in range(N):
    p=sphere(color=color.blue,radius=0.2, pos=vec(random(),random(),random()))
print(p)

if(N>118):nom1=text(text="No existe ese elemento", pos=vec(0,10,-10))
if(N==1):nom1=text(text="Hidrogeno[H]", pos=vec(0,10,-10))
if(N==2):nom1=text(text="Helio[He]", pos=vec(0,10,-10))
if(N==3):nom1=text(text="Litio[Li]", pos=vec(0,10,-10))
if(N==4):nom1=text(text="Berilio[Be]", pos=vec(0,10,-10))
if(N==5):nom1=text(text="Boro[B]", pos=vec(0,10,-10))
if(N==6):nom1=text(text="Carbono[C]", pos=vec(0,10,-10))
if(N==7):nom1=text(text="Nitrogeno[N]", pos=vec(0,10,-10))
if(N==8):nom1=text(text="Oxigeno[O]", pos=vec(0,10,-10))
if(N==9):nom1=text(text="Fluor[F]", pos=vec(0,10,-10))
if(N==10):nom1=text(text="Neon[Ne]", pos=vec(0,10,-10))
if(N==11):nom1=text(text="Sodio[Na]", pos=vec(0,10,-10))
if(N==12):nom1=text(text="Magnesio[Mg]", pos=vec(0,10,-10))
if(N==13):nom1=text(text="Aluminio[Al]", pos=vec(0,10,-10))
if(N==14):nom1=text(text="Silicio[Si]", pos=vec(0,10,-10))
if(N==15):nom1=text(text="Fosforo[P]", pos=vec(0,10,-10))
if(N==16):nom1=text(text="Azufre[S]", pos=vec(0,10,-10))
if(N==17):nom1=text(text="Cloro[Cl]", pos=vec(0,10,-10))
if(N==18):nom1=text(text="Argon[Ar]", pos=vec(0,10,-10))
if(N==19):nom1=text(text="Potasio[K]", pos=vec(0,10,-10))
if(N==20):nom1=text(text="Calcio[Ca]", pos=vec(0,10,-10))
if(N==21):nom1=text(text="Escandio[Sc]", pos=vec(0,10,-10))
if(N==22):nom1=text(text="Titanio[Ti]", pos=vec(0,10,-10))
if(N==23):nom1=text(text="Vanadio[V]", pos=vec(0,10,-10))
if(N==24):nom1=text(text="Cromo[Cr]", pos=vec(0,10,-10))
if(N==25):nom1=text(text="Manganesio[Mn]", pos=vec(0,10,-10))
if(N==26):nom1=text(text="Hierro[Fe]", pos=vec(0,10,-10))
if(N==27):nom1=text(text="Cobalto[Co]", pos=vec(0,10,-10))
if(N==28):nom1=text(text="Niquel[Ni]", pos=vec(0,10,-10))
if(N==29):nom1=text(text="Cobre[Cu]", pos=vec(0,10,-10))
if(N==30):nom1=text(text="Zinc[Zn]", pos=vec(0,10,-10))
if(N==31):nom1=text(text="Galio[Ga]", pos=vec(0,10,-10))
if(N==32):nom1=text(text="Germanio[Ge]", pos=vec(0,10,-10))
if(N==33):nom1=text(text="Arsenico[As]", pos=vec(0,10,-10))
if(N==34):nom1=text(text="Selenio[Se]", pos=vec(0,10,-10))
if(N==35):nom1=text(text="Bromo[Br]", pos=vec(0,10,-10))
if(N==36):nom1=text(text="Kripton[Kr]", pos=vec(0,10,-10))
if(N==37):nom1=text(text="Rubidio[Rb]", pos=vec(0,10,-10))
if(N==38):nom1=text(text="Estroncio[Sr]", pos=vec(0,10,-10))
if(N==39):nom1=text(text="Itrio[Y]", pos=vec(0,10,-10))
if(N==40):nom1=text(text="Zirconio[Zr]", pos=vec(0,10,-10))
if(N==41):nom1=text(text="Niobio[Nb]", pos=vec(0,10,-10))
if(N==42):nom1=text(text="Molibdeno[Mo]", pos=vec(0,10,-10))
if(N==43):nom1=text(text="Tecnecio[Tc]", pos=vec(0,10,-10))
if(N==44):nom1=text(text="Rutenio[Ru]", pos=vec(0,10,-10))
if(N==45):nom1=text(text="Rodio[Rh]", pos=vec(0,10,-10))
if(N==46):nom1=text(text="Paladio[Pd]", pos=vec(0,10,-10))
if(N==47):nom1=text(text="Plata[Ag]", pos=vec(0,10,-10))
if(N==48):nom1=text(text="Cadmio[Cd]", pos=vec(0,10,-10))
if(N==49):nom1=text(text="Indio[In]", pos=vec(0,10,-10))
if(N==50):nom1=text(text="Estaño[Sn]", pos=vec(0,10,-10))
if(N==51):nom1=text(text="Antimonio[Sb]", pos=vec(0,10,-10))
if(N==52):nom1=text(text="Telurio[Te]", pos=vec(0,10,-10))
if(N==53):nom1=text(text="Yodo[I]", pos=vec(0,10,-10))
if(N==54):nom1=text(text="Xenon[Xe]", pos=vec(0,10,-10))
if(N==55):nom1=text(text="Cesio[Cs]", pos=vec(0,10,-10))
if(N==56):nom1=text(text="Bario[Ba]", pos=vec(0,10,-10))
if(N==57):nom1=text(text="Lantano[La]", pos=vec(0,10,-10))
if(N==58):nom1=text(text="Cerio[Ce]", pos=vec(0,10,-10))
if(N==59):nom1=text(text="Praseodimio[Pr]", pos=vec(0,10,-10))
if(N==60):nom1=text(text="Neodimio[Nd]", pos=vec(0,10,-10))
if(N==61):nom1=text(text="Prometio[Pm]", pos=vec(0,10,-10))
if(N==62):nom1=text(text="Samario[Sm]", pos=vec(0,10,-10))
if(N==63):nom1=text(text="Europio[Eu]", pos=vec(0,10,-10))
if(N==64):nom1=text(text="Gadolinio[Gd]", pos=vec(0,10,-10))
if(N==65):nom1=text(text="Terbio[Tb]", pos=vec(0,10,-10))
if(N==66):nom1=text(text="Disprosio[Dy]", pos=vec(0,10,-10))
if(N==67):nom1=text(text="Holmio[Ho]", pos=vec(0,10,-10))
if(N==68):nom1=text(text="Erbio[Er]", pos=vec(0,10,-10))
if(N==69):nom1=text(text="Tulio[Tm]", pos=vec(0,10,-10))
if(N==70):nom1=text(text="Yterbio[Yb]", pos=vec(0,10,-10))
if(N==71):nom1=text(text="Lutecio[Lu]", pos=vec(0,10,-10))
if(N==72):nom1=text(text="Hafnio[Hf]", pos=vec(0,10,-10))
if(N==73):nom1=text(text="Tantalo[Ta]", pos=vec(0,10,-10))
if(N==74):nom1=text(text="Wolframio[W]", pos=vec(0,10,-10))
if(N==75):nom1=text(text="Renio[Re]", pos=vec(0,10,-10))
if(N==76):nom1=text(text="Osmio[Os]", pos=vec(0,10,-10))
if(N==77):nom1=text(text="Iridio[Ir]", pos=vec(0,10,-10))
if(N==78):nom1=text(text="Platino[Pt]", pos=vec(0,10,-10))
if(N==79):nom1=text(text="Oro[Au]", pos=vec(0,10,-10))
if(N==80):nom1=text(text="Mercurio[Hg]", pos=vec(0,10,-10))
if(N==81):nom1=text(text="Talio[Tl]", pos=vec(0,10,-10))
if(N==82):nom1=text(text="Plomo[Pb]", pos=vec(0,10,-10))
if(N==83):nom1=text(text="Bismuto[Bi]", pos=vec(0,10,-10))
if(N==84):nom1=text(text="Polonio[Po]", pos=vec(0,10,-10))
if(N==85):nom1=text(text="Astato[At]", pos=vec(0,10,-10))
if(N==86):nom1=text(text="Radon[Rn]", pos=vec(0,10,-10))
if(N==87):nom1=text(text="Francio[Fr]", pos=vec(0,10,-10))
if(N==88):nom1=text(text="Radio[Ra]", pos=vec(0,10,-10))
if(N==89):nom1=text(text="Actinio[Ac]", pos=vec(0,10,-10))
if(N==90):nom1=text(text="Torio[Th]", pos=vec(0,10,-10))
if(N==91):nom1=text(text="Protactinio[Pa]", pos=vec(0,10,-10))
if(N==92):nom1=text(text="Uranio[U]", pos=vec(0,10,-10))
if(N==93):nom1=text(text="Neptunio[Np]", pos=vec(0,10,-10))
if(N==94):nom1=text(text="Plutonio[Pu]", pos=vec(0,10,-10))
if(N==95):nom1=text(text="Americio[Am]", pos=vec(0,10,-10))
if(N==96):nom1=text(text="Curio[Cm]", pos=vec(0,10,-10))
if(N==97):nom1=text(text="Berquelio[Bk]", pos=vec(0,10,-10))
if(N==98):nom1=text(text="Californio[Cf]", pos=vec(0,10,-10))
if(N==99):nom1=text(text="Einstenio[Es]", pos=vec(0,10,-10))
if(N==100):nom1=text(text="Fermio[Fm]", pos=vec(0,10,-10))
if(N==101):nom1=text(text="Mendeleievo[Md]", pos=vec(0,10,-10))
if(N==102):nom1=text(text="Nobelio[No]", pos=vec(0,10,-10))
if(N==103):nom1=text(text="Laurencio[Lr]", pos=vec(0,10,-10))
if(N==104):nom1=text(text="Rutherfordio[Rf]", pos=vec(0,10,-10))
if(N==105):nom1=text(text="Dubnio[Db]", pos=vec(0,10,-10))
if(N==106):nom1=text(text="Seaborgio[Sg]", pos=vec(0,10,-10))
if(N==107):nom1=text(text="Bohrio[Bh]", pos=vec(0,10,-10))
if(N==108):nom1=text(text="Hassio[Hs]", pos=vec(0,10,-10))
if(N==109):nom1=text(text="Meitnerio[Mt]", pos=vec(0,10,-10))
if(N==110):nom1=text(text="Darmstadtio[Ds]", pos=vec(0,10,-10))
if(N==111):nom1=text(text="Roentgenio[Rg]", pos=vec(0,10,-10))
if(N==112):nom1=text(text="Copernicio[Cn]", pos=vec(0,10,-10))
if(N==113):nom1=text(text="Nihonio[Nh]", pos=vec(0,10,-10))
if(N==114):nom1=text(text="Flerovio[Fl]", pos=vec(0,10,-10))
if(N==115):nom1=text(text="Moscovio[Mc]", pos=vec(0,10,-10))
if(N==116):nom1=text(text="Livermorio[Lv]", pos=vec(0,10,-10))
if(N==117):nom1=text(text="Teneso[Ts]", pos=vec(0,10,-10))
if(N==118):nom1=text(text="Oganeson[Og]", pos=vec(0,10,-10))

E=[sphere(pos =vec(1+5*random(),1+5*random(),1+5*random()), radius = 0.1, make_trail=True,color =color.red,interval=1, retain=50)for i in range(N)]
        
        
sleep(3)
for k in range(N):
    for o in range(2000):
        rate(100)
        a=o*T
        phi=0
        a1=a1+0.002
        if(N>0):
            for i,e in enumerate(E):
                E[i].pos=((-1)**i)*vec(ro*sin(a+pi*i)*cos(phi+pi*(-1*i)),ro*cos(a)*sin(a1+2*i+((-1)**i)*pi),ro*cos(a+ro**3*(4/3)*pi*i))
  

    



  




