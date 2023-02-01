from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd

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



disease=['Mantar Enfeksiyonu','Alerji','Reflü','Kronik Kolestaz','İlaç Reaksiyonu',
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
# tr=pd.read_csv("Testing.csv")
tr=pd.read_csv("Data_EXCEL/testing_csv.csv", encoding='utf8')
tr.replace({'tehsis':{'Mantar Enfeksiyonu':0,'Alerji':1,'Reflü':2,'Kronik Kolestaz':3,'İlaç Reaksiyonu':4,
            'Peptik Ülser':5,'AIDS':6,'Şeker':7,'Bağırsak Enfeksiyonu':8,'Bronşiyal Astım':9,'Hipertansiyon':10,
            'Migren':11,'Boyun Kireçlenmesi':12,
            'Felç (Beyin Kanaması)':13,'Sarılık':14,'Sıtma':15,'Çiçeği':16,'Dang Humması':17,'Tifo':18,'Hepatit A':19,
            'Hepatit B':20,'Hepatit C':21,'Hepatit D':22,'Hepatit E':23,'Alkolik Hepatit':24,'Tüberküloz':25,
            'Soğuk Algınlığı':26,'Pnömoni (Zatürre)':27,'Hemoroid':28,'Kalp Krizi':29,'Varis Damar':30,'Hipotiroidi':31,
            'Hipertiroidi':32,'Hipoglisemi':33,'Kireçlenme':34,'Artrit':35,
            'Vertigo':36,'Akne':37,'İdrar Yolu Enfeksiyonu':38,'Sedef':39,
            'İmpetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["tehsis"]]
np.ravel(y_test)

# TRAINING DATA
df=pd.read_csv("Data_EXCEL/dataset_csv.csv",  encoding='utf8')

df.replace({'tehsis':{'Mantar Enfeksiyonu':0,'Alerji':1,'Reflü':2,'Kronik Kolestaz':3,'İlaç Reaksiyonu':4,
            'Peptik Ülser':5,'AIDS':6,'Şeker':7,'Bağırsak Enfeksiyonu':8,'Bronşiyal Astım':9,'Hipertansiyon':10,
            'Migren':11,'Boyun Kireçlenmesi':12,
            'Felç (Beyin Kanaması)':13,'Sarılık':14,'Sıtma':15,'Su Çiçeği':16,'Dang Humması':17,'Tifo':18,'Hepatit A':19,
            'Hepatit B':20,'Hepatit C':21,'Hepatit D':22,'Hepatit E':23,'Alkolik Hepatit':24,'Tüberküloz':25,
            'Soğuk Algınlığı':26,'Pnömoni (Zatürre)':27,'Hemoroid':28,'Kalp Krizi':29,'Varis Damar':30,'Hipotiroidi':31,
            'Hipertiroidi':32,'Hipoglisemi':33,'Kireçlenme':34,'Artrit':35,
            'Vertigo':36,'Akne':37,'İdrar Yolu Enfeksiyonu':38,'Sedef':39,
            'İmpetigo':40}},inplace=True)

X = df[l1]

y = df[["tehsis"]]

print (y)

for inte in y:
    if(int(inte) < 0 | int(inte) > 40):
        print (inte)
