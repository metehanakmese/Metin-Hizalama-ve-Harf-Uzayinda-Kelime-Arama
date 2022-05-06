alfabetik_sozluk={"A":1,"B":2,"C":3,"Ç":4,"D":5,"E":6,"F":7,"G":8,"Ğ":9,"H":10,"I":11,"İ":12,"J":13,"K":14,"L":15,"M":16,"N":17,"O":18,"Ö":19,"P":20,"R":21,"S":22,"Ş":23,"T":24,"U":25,"Ü":26,"V":27,"Y":28,"Z":29}
def sayi_al(alt_sinir,ust_sinir):
    try:
        sayi=int(input())
        hatali_giris=False
    except ValueError:
        hatali_giris=True
    while hatali_giris==True or sayi<alt_sinir or sayi>ust_sinir:
        try:
            sayi=int(input("Hatalı veri girişi! Lütfen tekrar giriniz: "))
            hatali_giris=False
        except ValueError:
            hatali_giris=True
    return sayi

def evet_hayir_al():
    cevap = input()
    while cevap not in "eEhH":
        cevap = input("Hatalı veri girişi! Lütfen tekrar giriniz: ")
    return cevap
def buyut(metin):
    buyutulmus_metin=""
    for harf in metin:
        if harf=="ç":
            buyutulmus_metin+="Ç"
        elif harf=="ğ":
            buyutulmus_metin+="Ğ"
        elif harf=="i":
            buyutulmus_metin+="İ"
        elif harf=="ö":
            buyutulmus_metin+="Ö"
        elif harf=="ş":
            buyutulmus_metin+="Ş"
        elif harf=="ü":
            buyutulmus_metin+="Ü"
        else:
            buyutulmus_metin+=harf.upper()
    return buyutulmus_metin

def sırala(liste):
    for i in range(len(liste)):
        for j in range(len(liste)-i-1):
            ilk_kelime=liste[j][0]
            ikinci_kelime=liste[j+1][0]
            if alfabetik_sozluk[ilk_kelime[0]]>alfabetik_sozluk[ikinci_kelime[0]]:
                liste[j],liste[j+1]=liste[j+1],liste[j]
            elif alfabetik_sozluk[ilk_kelime[0]]==alfabetik_sozluk[ikinci_kelime[0]]:
                if len(ilk_kelime)>len(ikinci_kelime):
                    for k in range(1,len(ikinci_kelime)):
                        if alfabetik_sozluk[ilk_kelime[k]]>alfabetik_sozluk[ikinci_kelime[k]]:
                            liste[j],liste[j+1]=liste[j+1],liste[j]
                            break
                    else:
                        liste[j],liste[j+1]=liste[j+1],liste[j]
                elif len(ilk_kelime)==len(ikinci_kelime):
                    for k in range(1,len(ikinci_kelime)):
                        if alfabetik_sozluk[ilk_kelime[k]]>alfabetik_sozluk[ikinci_kelime[k]]:
                            liste[j],liste[j+1]=liste[j+1],liste[j]
                            break
                else:
                    for k in range(1,len(ilk_kelime)):
                        if alfabetik_sozluk[ilk_kelime[k]]>alfabetik_sozluk[ikinci_kelime[k]]:
                            liste[j],liste[j+1]=liste[j+1],liste[j]
                            break
    return liste
def iki_boyutlu_liste_yarat(sutun_sayisi,satir_sayisi):
    iki_boyutlu_liste=[]
    for i in range(satir_sayisi):
        bir_liste=[0]*sutun_sayisi
        iki_boyutlu_liste.append(bir_liste)
    return iki_boyutlu_liste
genel_tekrar_sozlugu={}
genel_tekrar_listesi=[]
devam="E"
while devam.upper()=="E":
    metin=input("Metninizi giriniz: ")
    metin=buyut(metin)
    kelimeler=[]
    for kelime in metin.split("-"):
        kelimeler.append(kelime)
    harf_sayilari = []
    for i in range(len(kelimeler)):
        harf_sayilari.append(len(kelimeler[i]))
    kelime_tekrar_sozlugu={}
    for i in range(len(kelimeler)):
        kelime_tekrar_sozlugu[kelimeler[i]]=kelime_tekrar_sozlugu.get(kelimeler[i],0)+1
        genel_tekrar_sozlugu[kelimeler[i]]=genel_tekrar_sozlugu.get(kelimeler[i],0)+1
    kelime_tekrar_listesi=[]
    for key,value in kelime_tekrar_sozlugu.items():
        kelime_tekrar_listesi.append([key,value])
    print("Paragrafın görüntülenmesini istediğiniz satır genişliğini giriniz: ",end="")
    satir_genisligi=sayi_al(0,9999999)
    while satir_genisligi!=0:
        yeni_metin=""
        toplam,index,baslangic_indexi,son_index,bir_onceki_index,kelimeler_arasi_bosluk=0,0,0,0,0,0
        satir_sayisi=1
        while toplam<=satir_genisligi and index<len(harf_sayilari):
            toplam+=harf_sayilari[index]+kelimeler_arasi_bosluk
            if toplam<satir_genisligi:
                toplam-=kelimeler_arasi_bosluk
            if toplam>=satir_genisligi:
                if toplam>satir_genisligi:
                    index=bir_onceki_index
                    toplam-=harf_sayilari[index+1]+1
                    kelimeler_arasi_bosluk-=1
                bosluk_sayisi=satir_genisligi-toplam
                if bosluk_sayisi%(kelimeler_arasi_bosluk)!=0:
                    if satir_sayisi%2==1:
                        dagitilan_bosluk_sayisi=bosluk_sayisi%(kelimeler_arasi_bosluk)
                    else:
                        dagitilmamasi_gereken_bosluk=(index-baslangic_indexi)-(bosluk_sayisi%(index-baslangic_indexi))
                for i in range(baslangic_indexi,index+1):
                    if bosluk_sayisi>0 and i<index:
                        if bosluk_sayisi%(kelimeler_arasi_bosluk)==0:
                            yeni_metin+=kelimeler[i]+(bosluk_sayisi//(kelimeler_arasi_bosluk)+1)*" "
                        else:
                            if satir_sayisi%2==1:
                                if dagitilan_bosluk_sayisi!=0:
                                    yeni_metin+=kelimeler[i]+(bosluk_sayisi//(kelimeler_arasi_bosluk)+2)*" "
                                    dagitilan_bosluk_sayisi-=1
                                else:
                                    yeni_metin+=kelimeler[i]+(bosluk_sayisi//(kelimeler_arasi_bosluk)+1)*" "
                            else:
                                if dagitilmamasi_gereken_bosluk!=0:
                                    yeni_metin+=kelimeler[i]+(bosluk_sayisi//(kelimeler_arasi_bosluk)+1)*" "
                                    dagitilmamasi_gereken_bosluk-=1
                                else:
                                    yeni_metin+=kelimeler[i]+(bosluk_sayisi//(kelimeler_arasi_bosluk)+2)*" "
                    elif bosluk_sayisi==0 and i<index:
                        yeni_metin+=kelimeler[i]+" "
                    if i==index:
                        yeni_metin+=kelimeler[i]+"\n"
                        satir_sayisi+=1
                        kelimeler_arasi_bosluk=-1
                        son_index=index
                baslangic_indexi=index+1
                toplam=0
            bir_onceki_index=index
            index+=1
            kelimeler_arasi_bosluk+=1
        for x in range(son_index+1,len(kelimeler)):
            yeni_metin+=kelimeler[x]+" "
        print(yeni_metin)
        print("")
        print("Paragrafın görüntülenmesini istediğiniz satır genişliğini giriniz: ",end="")
        satir_genisligi=sayi_al(0,9999999)
    index_0_sort=[]
    sırala(kelime_tekrar_listesi)
    for i in range(len(kelime_tekrar_listesi)):
        index_0_sort.append(kelime_tekrar_listesi[i])
    kelime_tekrar_listesi.sort(key=lambda liste:liste[1],reverse=True)
    print("Kelime               Tekrar Say        |        Kelime               Tekrar Say ")
    print("-------------------  ----------        |        -------------------  ---------- ")
    for i in range(len(index_0_sort)):
        print(format(index_0_sort[i][0],"20"),end=" ")
        print(format(index_0_sort[i][1],"2"),end="        ")
        print("        |        ",end="")
        print(format(kelime_tekrar_listesi[i][0],"20")," ",end="")
        print(format(kelime_tekrar_listesi[i][1]))
    print("Başka bir paragraf girmek ister misiniz?: ",end="")
    devam=evet_hayir_al().upper()
for key,value in genel_tekrar_sozlugu.items():
    genel_tekrar_listesi.append([key,value])
genel_0_sort=[]
sırala(genel_tekrar_listesi)
for i in range(len(genel_tekrar_listesi)):
    genel_0_sort.append(genel_tekrar_listesi[i])
genel_tekrar_listesi.sort(key=lambda liste:liste[1],reverse=True)
print("Kelime               Tekrar Say        |        Kelime               Tekrar Say ")
print("-------------------  ----------        |        -------------------  ---------- ")
for i in range(len(genel_0_sort)):
    print(format(genel_0_sort[i][0], "20"), end=" ")
    print(format(genel_0_sort[i][1], "2"), end="        ")
    print("        |        ", end="")
    print(format(genel_tekrar_listesi[i][0], "20"), " ", end="")
    print(format(genel_tekrar_listesi[i][1]))
konuma_gore_dizilis=iki_boyutlu_liste_yarat(20,29)
toplam_harf_sayisi=[0]*29
for i in range(len(genel_tekrar_listesi)):
    gecici_kelime=genel_tekrar_listesi[i][0]
    for j in range(len(genel_tekrar_listesi[i][0])):
        konuma_gore_dizilis[alfabetik_sozluk[gecici_kelime[j]]-1][j]+=genel_tekrar_listesi[i][1]
        toplam_harf_sayisi[alfabetik_sozluk[gecici_kelime[j]]-1]+=genel_tekrar_listesi[i][1]
print("       Kelime içindeki konum")
print("Harf",end="  ")
for i in range(20):
    print(format(i+1,"3"),end="  ")
print("Toplam")
print("----",end="  ")
for i in range(20):
    print("---",end="  ")
print("------")
a=0
for key,value in alfabetik_sozluk.items():
    print(format(key,"1"),end="     ")
    for i in range(20):
        print(format(konuma_gore_dizilis[a][i],"3"),end="  ")
    print(format(toplam_harf_sayisi[a],"3"))
    a+=1
def uzayda_kelime_ara(kelime,harf_uzayi):
    liste=[]
    for i in range(len(harf_uzayi)):
        for j in range(len(harf_uzayi)):
            if kelime[0]==harf_uzayi[i][j]:
                if i>=len(kelime)-1:
                    dogruluk1=1
                    onceki_dogruluk1=0
                    for k in range(1, len(kelime)):
                        if harf_uzayi[i-k][j]==kelime[k] and dogruluk1==onceki_dogruluk1+1:
                            onceki_dogruluk1=dogruluk1
                            dogruluk1+=1
                        else:
                            onceki_dogruluk1+=1
                    if dogruluk1==len(kelime):
                        liste.append((i+1,j+1,1))
                if i>=len(kelime)-1 and j<=len(harf_uzayi)-len(kelime):
                    dogruluk2=1
                    onceki_dogruluk2=0
                    for k in range(1,len(kelime)):
                        if harf_uzayi[i-k][j+k]==kelime[k] and dogruluk2==onceki_dogruluk2+1:
                            onceki_dogruluk2=dogruluk2
                            dogruluk2+=1
                        else:
                            onceki_dogruluk2+=1
                    if dogruluk2==len(kelime):
                        liste.append((i+1,j+1,2))
                if j<=len(harf_uzayi)-len(kelime):
                    dogruluk3=1
                    onceki_dogruluk3=0
                    for k in range(1,len(kelime)):
                        if harf_uzayi[i][j+k]==kelime[k] and dogruluk3==onceki_dogruluk3+1:
                            onceki_dogruluk3=dogruluk3
                            dogruluk3+=1
                        else:
                            onceki_dogruluk3+=1
                    if dogruluk3==len(kelime):
                        liste.append((i+1,j+1,3))
                if i<=len(harf_uzayi)-len(kelime) and j<=len(harf_uzayi)-len(kelime):
                    dogruluk4=1
                    onceki_dogruluk4=0
                    for k in range(1,len(kelime)):
                        if harf_uzayi[i+k][j+k] == kelime[k] and dogruluk4==onceki_dogruluk4+1:
                            onceki_dogruluk4=dogruluk4
                            dogruluk4 += 1
                        else:
                            onceki_dogruluk4+=1
                    if dogruluk4==len(kelime):
                        liste.append((i+1,j+1,4))
                if i<=len(harf_uzayi)-len(kelime):
                    dogruluk5=1
                    onceki_dogruluk5=0
                    for k in range(1,len(kelime)):
                        if harf_uzayi[i+k][j]==kelime[k] and dogruluk5==onceki_dogruluk5+1:
                            onceki_dogruluk5=dogruluk5
                            dogruluk5 += 1
                        else:
                            onceki_dogruluk5+=1
                    if dogruluk5==len(kelime):
                        liste.append((i+1,j+1,5))
                if i<=len(harf_uzayi)-len(kelime) and j>=len(kelime)-1:
                    dogruluk6=1
                    onceki_dogruluk6=0
                    for k in range(1,len(kelime)):
                        if harf_uzayi[i+k][j-k]==kelime[k] and dogruluk6==onceki_dogruluk6+1:
                            onceki_dogruluk6=dogruluk6
                            dogruluk6+=1
                        else:
                            onceki_dogruluk6+=1
                    if dogruluk6==len(kelime):
                        liste.append((i+1,j+1,6))
                if j>=len(kelime)-1:
                    dogruluk7=1
                    onceki_dogruluk7=0
                    for k in range(1,len(kelime)):
                        if harf_uzayi[i][j-k]==kelime[k] and dogruluk7==onceki_dogruluk7+1:
                            onceki_dogruluk7=dogruluk7
                            dogruluk7+=1
                        else:
                            onceki_dogruluk7+=1
                    if dogruluk7==len(kelime):
                        liste.append((i+1,j+1,7))
                if i>=len(kelime)-1 and j>=len(kelime)-1:
                    dogruluk8=1
                    onceki_dogruluk8=0
                    for k in range(1,len(kelime)):
                        if harf_uzayi[i-k][j-k]==kelime[k] and dogruluk8==onceki_dogruluk8+1:
                            onceki_dogruluk8=dogruluk8
                            dogruluk8+=1
                        else:
                            onceki_dogruluk8+=1
                    if dogruluk8==len(kelime):
                        liste.append((i+1,j+1,8))
    return liste

harf_uzayi=[]
harf_uzayi_dosyasi=open("harf_uzayi.txt","r",encoding="UTF-8")
harfler=harf_uzayi_dosyasi.readline().replace("\n","")
while harfler!="":
    bir_liste=[]
    for i in range(len(harfler)):
        bir_liste.append(harfler[i])
    harf_uzayi.append(bir_liste)
    harfler=harf_uzayi_dosyasi.readline().replace("\n","")
harf_uzayi_dosyasi.close()
sırala(genel_tekrar_listesi)
yon_listesi=[]
print("Kelime                  Satır No    Sütun No    Yönü   ")
print("--------------------    --------    --------    -------")
for i in range(len(genel_tekrar_listesi)):
    liste=uzayda_kelime_ara(genel_tekrar_listesi[i][0],harf_uzayi)
    if len(liste)==0:
        print(format(genel_tekrar_listesi[i][0],"20"),end="    ")
        print("Bulunamadı!")
    else:
        for j in range(len(liste)):
            print(format(genel_tekrar_listesi[i][0],"20"),end="    ")
            print(format(liste[j][0],"4"),end="        ")
            print(format(liste[j][1],"4"),end="        ")
            if liste[j][2]==1:
                print("Kuzey")
            elif liste[j][2]==2:
                print("Kuzeydğu")
            elif liste[j][2] == 3:
                print("Doğu")
            elif liste[j][2]==4:
                print("Güneydoğu")
            elif liste[j][2] == 5:
                print("Güney")
            elif liste[j][2]==6:
                print("Güneybatı")
            elif liste[j][2] == 7:
                print("Batı")
            elif liste[j][2]==8:
                print("Kuzeybatı")

