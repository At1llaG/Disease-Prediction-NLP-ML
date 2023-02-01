from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

l1=['kasinti','deri_dokuntusu','nodal_deri_dokuntuleri','surekli_hapsirma','titreme','titreme_nobeti','eklem_agrisi',
    'mide_agrisi','asitlik','dilde_ulserler','kas_erimesi','kusma','agrili_idrara_cikma','idarda_kan','yorgunluk',
    'kilo_alma','kaygi','ellerde_ve_ayaklarda_sogukluk','ani_duygu_degisimi','kilo_kaybi','huzursuzluk','uyusukluk','bademcik_yaralari',
    'duzensiz_seker_seviyesi','oksuruk','yuksek_ates','gozlerde_cokukluk','nefes_darligi','terlemek','sivi_kaybi','hazimsizlik',
    'bas_agrisi','ciltte_sararma','koyu_idrar','mide_bulantisi ','istah_kaybi','goz_arkasinda_agri','sirt_agrisi','kabizlik',
    'bel_agrisi','ishal','hafif_ates','sari_idrar','gozlerin_sararmasi','akut_karaciger_yetmezligi','asiri_sivi_yuklenmesi',
    'midede_siskinlik','sismis_lenf_dugumleri','halsizlik','bulanik_ve_bozuk_gorus','balgam','bogazda_tahris',
    'gozlerde_kizarma','sinus_basinci','burun_akmasi','tikaniklik','gogus_agrisi','uzuvlarda_zayiflik','hizli_kalp_atisi',
    'bagirsak_hareketleri_sirasinda_agri','anal_bolgede_agri','kanli_diski','anuste_tahris','boyun_agrisi','bas_donmesi','kramplar',
    'morarma','obezite','bacaklarda_sisme','kan_damarlarinda_sisme','yuz_ve_gozlerde_kabariklik','tiroitte_buyume','tirnaklarda_kirilganlik',
    'uzuvlarda_sisme','asiri_aclik','evlilik_disi_iliski','dudaklarda_kuruma_ve_karincalanma','konusma_bozuklugu','diz_agrisi','kalca_ekleminde_agri',
    'kas_gucsuzlugu','boyun_tutulmasi','eklemlerde_sisme','hareketlerde_zorlanma','hareketlerde_bukulme','denge_kaybi','sabit_olamama','vucudun_bir_tarafinda_gucsuzluk',
    'koku_kaybi','mesane _rahatsizligi','idrarin_kotu_kokmasi','surekli_idrar_hissi','gaz_kacirma','ic_kasinti','kiskirtici_olma',
    'depresyon','sinirlilik','kas_agrisi','net_dusunememe','vucut_uzerinde_kirmizi_noktalar','karin_agrisi','anormal_adet_gorme','deride_pigment_bozuklugu',
    'gozlerin_sulanmasi','istah_artisi','asiri_idrar_cikisi','aile_gecmisi','mukuslu_balgam','pasli_balgam','konsantrasyon_eksikligi','gorsel_rahatsizliklar',
    'kan _nakli_almak','steril_olmayan_enjeksiyonlar_almak','koma','mide_kanamasi','karin_siskinligi','alkol_tuketimi_oykusu',
    'asiri_sivi_yuklenmesi','balgamda_kan','baldirda_belirgin_damarlar','carpinti','agrili_yuruyus','iltihapli_sivilce_cikmasi','siyah_noktalar','yuzde_kasinti','ciltte_soyulma',
    'cilt_renginde_degisme','tirnaklarda_kucuk_ezikler','iltihapli_tirnaklar','su_toplama','burun_cevresinde_kirmizi_yara','deride_kabuklu_yaralar']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

hastalik=['Mantar Enfeksiyonu','Alerji','Reflü','Kronik Kolestaz','İlaç Reaksiyonu',
        'Peptik Ülser','AIDS','Şeker','Bağırsak Enfeksiyonu','Bronşiyal Astım','Hipertansiyon',
        'Migren','Boyun Kireçlenmesi',
        'Felç (Beyin Kanaması)','Sarılık','Sıtma','Su Çiçeği','Dang Humması','Tifo','Hepatit A',
        'Hepatit B','Hepatit C','Hepatit D','Hepatit E','Alkolik Hepatit','Tüberküloz',
        'Soğuk Algınlığı','Pnömoni (Zatürre)','Hemoroid',
        'Kalp Krizi','Varis Damar','Hipotiroidi','Hipertiroidi','Hipoglisemi','Kireçlenme',
        'Artrit','Vertigo','Akne','İdrar Yolu Enfeksiyonu','Sedef',
        'İmpetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA
tr=pd.read_csv("CSV_Data/Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

# TRAINING DATA
df=pd.read_csv("CSV_Data/Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)


def NaiveBayes(l2):
    gnb = MultinomialNB()
    gnb=gnb.fit(X,np.ravel(y))
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

    
    #psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    #for k in range(0,len(l1)):
    #    for z in psymptoms:
    #        if(z==l1[k]):
    #            l2[k]=1

    
    
    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(disease[predicted] == disease[a]):
            h='yes'
            break

    if (h=='yes'):
        return (hastalik[a])
    else:
        return "No Disease"

    #if (h=='yes'):
    #    t3.delete("1.0", END)
    #    t3.insert(END, disease[a])
    #else:
    #    t3.delete("1.0", END)
    #    t3.insert(END, "No Disease")

