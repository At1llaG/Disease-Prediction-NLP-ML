


from app_test2 import NaiveBayes






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


test1 = [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
test2 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

result = NaiveBayes(test2)



print (result)
