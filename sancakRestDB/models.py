# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Deviraldigim(models.Model):
    deviraldim = models.IntegerField(db_column='DevirAldim')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DevirAldigim'
        verbose_name_plural = 'DevirAldigim'

    def __str__(self):
        return "Miktar: " + str(self.deviraldim)


class Disiplin(models.Model):
    disiplin_id = models.AutoField(db_column='Disiplin_id', primary_key=True)  # Field name made lowercase.
    adisoyadi = models.CharField(db_column='AdiSoyadi', max_length=50)  # Field name made lowercase.
    ehliyetno = models.IntegerField(db_column='EhliyetNo')  # Field name made lowercase.
    tarih = models.DateField(db_column='Tarih')  # Field name made lowercase.
    uyarisayisi = models.IntegerField(db_column='UyariSayisi')  # Field name made lowercase.
    uyariraporu = models.CharField(db_column='UyariRaporu', max_length=100)  # Field name made lowercase.
    mecliskarari = models.CharField(db_column='MeclisKarari', max_length=1000)  # Field name made lowercase.
    aciklama = models.CharField(db_column='Aciklama', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disiplin'
        verbose_name_plural = 'Disiplin Cezalari'

    def __str__(self):
        return self.adisoyadi + " " + str(self.tarih)


class Etkinliksurus(models.Model):
    etkinlik_id = models.AutoField(db_column='Etkinlik_Id', primary_key=True)  # Field name made lowercase.
    etkinlikadi = models.CharField(db_column='EtkinlikAdi', max_length=50)  # Field name made lowercase.
    etkinliktarihi = models.DateField(db_column='EtkinlikTarihi')  # Field name made lowercase.
    etkinlikkatilim = models.IntegerField(db_column='EtkinlikKatilim')  # Field name made lowercase.
    aciklama = models.CharField(db_column='Aciklama', max_length=500)  # Field name made lowercase.
    etkinlikyapildimi = models.CharField(db_column='EtkinlikYapildiMi', max_length=75)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EtkinlikSurus'
        verbose_name_plural = 'Surus Etkinlikleri'

    def __str__(self):
        return self.etkinlikadi + " " + str(self.etkinliktarihi)


class Giris(models.Model):
    kullanici_id = models.AutoField(db_column='Kullanici_id', primary_key=True)  # Field name made lowercase.
    ehliyetno = models.IntegerField(db_column='EhliyetNo')  # Field name made lowercase.
    sifre = models.CharField(db_column='Sifre', max_length=10)  # Field name made lowercase.
    yetki = models.IntegerField(db_column='Yetki')  # Field name made lowercase.
    gorevi = models.CharField(db_column='Gorevi', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Giris'
        verbose_name_plural = 'Giris'


class Girislog(models.Model):
    log_id = models.AutoField(db_column='Log_id', primary_key=True)  # Field name made lowercase.
    tarih = models.CharField(db_column='Tarih', max_length=50)  # Field name made lowercase.
    ehliyetno = models.CharField(db_column='EhliyetNo', max_length=20)  # Field name made lowercase.
    derece = models.CharField(db_column='Derece', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GirisLog'
        verbose_name_plural = 'Giris Kayitlari'

    def __str__(self):
        return "Kisi:" + self.ehliyetno + " Tarih:" + str(self.tarih)


class Harcamalar(models.Model):
    harcamatarih = models.DateField(db_column='HarcamaTarih')  # Field name made lowercase.
    nedenharcandi = models.CharField(db_column='NedenHarcandi', max_length=50)  # Field name made lowercase.
    harcananyer = models.CharField(db_column='HarcananYer', max_length=50)  # Field name made lowercase.
    harcamayapan = models.CharField(db_column='HarcamaYapan', max_length=50)  # Field name made lowercase.
    harcanantutar = models.CharField(db_column='HarcananTutar', max_length=11)  # Field name made lowercase.
    aciklama = models.CharField(db_column='Aciklama', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Harcamalar'
        verbose_name_plural = 'Harcamalar'

    def __str__(self):
        return "Nedeni: " + self.nedenharcandi + " Tutar:" + self.harcanantutar


class Kasaborc(models.Model):
    kasaborc_id = models.AutoField(db_column='KasaBorc_id', primary_key=True)  # Field name made lowercase.
    borctarihi = models.DateField(db_column='BorcTarihi')  # Field name made lowercase.
    adisoyadi = models.CharField(db_column='AdiSoyadi', max_length=25)  # Field name made lowercase.
    ehliyetno = models.IntegerField(db_column='EhliyetNo')  # Field name made lowercase.
    alinantutar = models.IntegerField(db_column='AlinanTutar')  # Field name made lowercase.
    alinmasebebi = models.CharField(db_column='AlinmaSebebi', max_length=100)  # Field name made lowercase.
    aciklama = models.CharField(db_column='Aciklama', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KasaBorc'
        verbose_name_plural = 'Karizma Takibi'

    def __str__(self):
        return self.adisoyadi + " Tutar:" + str(self.alinantutar) + " TL"


class Kmtakip(models.Model):
    km_id = models.AutoField(db_column='Km_id', primary_key=True)  # Field name made lowercase.
    adisoyadi = models.CharField(db_column='AdiSoyadi', max_length=25)  # Field name made lowercase.
    ehliyetno = models.CharField(db_column='EhliyetNo', max_length=10)  # Field name made lowercase.
    tarih = models.DateField(db_column='Tarih')  # Field name made lowercase.
    rotaturu = models.CharField(db_column='RotaTuru', max_length=20)  # Field name made lowercase.
    km = models.DecimalField(db_column='KM', max_digits=5, decimal_places=1)  # Field name made lowercase.
    rota = models.CharField(db_column='Rota', max_length=250)  # Field name made lowercase.
    aciklama = models.CharField(db_column='Aciklama', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KmTakip'
        verbose_name_plural = 'Kilometre Takibi'

    def __str__(self):
        return self.adisoyadi


class Kunye(models.Model):
    kunye_id = models.AutoField(db_column='Kunye_id', primary_key=True)  # Field name made lowercase.
    nick = models.CharField(db_column='Nick', max_length=15)  # Field name made lowercase.
    adisoyadi = models.CharField(db_column='AdiSoyadi', max_length=30)  # Field name made lowercase.
    dogumtarihi = models.DateField(db_column='DogumTarihi')  # Field name made lowercase.
    pozisyon = models.CharField(db_column='Pozisyon', max_length=15)  # Field name made lowercase.
    basvurutarihi = models.DateField(db_column='BasvuruTarihi')  # Field name made lowercase.
    kgiristarihi = models.DateField(db_column='KGirisTarihi')  # Field name made lowercase.
    meslegi = models.CharField(db_column='Meslegi', max_length=50)  # Field name made lowercase.
    yemintarihi = models.DateField(db_column='YeminTarihi')  # Field name made lowercase.
    ehliyetno = models.CharField(db_column='EhliyetNo', max_length=10, blank=True,
                                 null=True)  # Field name made lowercase.
    kangrubu = models.CharField(db_column='KanGrubu', max_length=5)  # Field name made lowercase.
    motormarka = models.CharField(db_column='MotorMarka', max_length=25)  # Field name made lowercase.
    motorcc = models.CharField(db_column='MotorCC', max_length=5)  # Field name made lowercase.
    plaka = models.CharField(db_column='Plaka', max_length=10)  # Field name made lowercase.
    telno = models.CharField(db_column='TelNo', max_length=15)  # Field name made lowercase.
    yakintelno = models.CharField(db_column='YakinTelNo', max_length=15)  # Field name made lowercase.
    yelekdontarihi = models.CharField(db_column='YelekDonTarihi', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kunye'
        verbose_name_plural = 'Kunye'

    def __str__(self):
        return self.adisoyadi + " (" + self.nick + ")"


class Meclis(models.Model):
    meclis_id = models.AutoField(db_column='Meclis_id', primary_key=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='Tarih')  # Field name made lowercase.
    konu = models.CharField(db_column='Konu', max_length=100)  # Field name made lowercase.
    alinankarar = models.CharField(db_column='AlinanKarar', max_length=800)  # Field name made lowercase.
    aciklama = models.CharField(db_column='Aciklama', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Meclis'
        verbose_name_plural = 'Meclis Kararlari'

    def __str__(self):
        return self.konu + " " + str(self.tarih)


class Pachyelek(models.Model):
    ehliyetno = models.IntegerField(db_column='EhliyetNo')  # Field name made lowercase.
    adisoyadi = models.CharField(db_column='AdiSoyadi', max_length=25)  # Field name made lowercase.
    verilmetarihi = models.DateField(db_column='VerilmeTarihi')  # Field name made lowercase.
    yelek = models.CharField(db_column='Yelek', max_length=5)  # Field name made lowercase.
    bayrak = models.CharField(db_column='Bayrak', max_length=5)  # Field name made lowercase.
    onsancak = models.CharField(db_column='OnSancak', max_length=5)  # Field name made lowercase.
    onkurukafa = models.CharField(db_column='OnKuruKafa', max_length=5)  # Field name made lowercase.
    chopper = models.CharField(db_column='Chopper', max_length=5)  # Field name made lowercase.
    mk = models.CharField(db_column='Mk', max_length=5)  # Field name made lowercase.
    bursa = models.CharField(db_column='Bursa', max_length=5)  # Field name made lowercase.
    sirtsancak = models.CharField(db_column='SirtSancak', max_length=5)  # Field name made lowercase.
    sirtkurukafa = models.CharField(db_column='SirtKuruKafa', max_length=5)  # Field name made lowercase.
    turkiye = models.CharField(db_column='Turkiye', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PachYelek'
        verbose_name_plural = 'Pach ve Yelek Takibi'

    def __str__(self):
        return self.adisoyadi


class Sayman(models.Model):
    sayman_id = models.AutoField(db_column='Sayman_id', primary_key=True)  # Field name made lowercase.
    adisoyadi = models.CharField(db_column='AdiSoyadi', max_length=30)  # Field name made lowercase.
    ehliyetno = models.IntegerField(db_column='EhliyetNo')  # Field name made lowercase.
    odemetarihi = models.DateField(db_column='OdemeTarihi')  # Field name made lowercase.
    odemesekli = models.CharField(db_column='OdemeSekli', max_length=25)  # Field name made lowercase.
    odenentl = models.DecimalField(db_column='OdenenTl', max_digits=5, decimal_places=1)  # Field name made lowercase.
    odemeaciklama = models.CharField(db_column='OdemeAciklama', max_length=30)  # Field name made lowercase.
    aciklama = models.CharField(db_column='Aciklama', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sayman'
        verbose_name_plural = 'Odemeler(Sayman)'

    def __str__(self):
        return self.adisoyadi + " Gerekce:" + str(self.odemesekli)


class Stok(models.Model):
    stok_id = models.AutoField(db_column='Stok_id', primary_key=True)  # Field name made lowercase.
    yeleksayisi = models.IntegerField(db_column='YelekSayisi')  # Field name made lowercase.
    fullpachsayisi = models.IntegerField(db_column='FullPachSayisi')  # Field name made lowercase.
    bayrak = models.IntegerField(db_column='Bayrak')  # Field name made lowercase.
    onsancak = models.IntegerField(db_column='OnSancak')  # Field name made lowercase.
    onkurukafa = models.IntegerField(db_column='OnKuruKafa')  # Field name made lowercase.
    chopper = models.IntegerField(db_column='Chopper')  # Field name made lowercase.
    mk = models.IntegerField(db_column='MK')  # Field name made lowercase.
    bursa = models.IntegerField(db_column='Bursa')  # Field name made lowercase.
    sirtsancak = models.IntegerField(db_column='SirtSancak')  # Field name made lowercase.
    sirtkurukafa = models.IntegerField(db_column='SirtKuruKafa')  # Field name made lowercase.
    turkiye = models.IntegerField(db_column='Turkiye')  # Field name made lowercase.
    stoktarihi = models.DateField(db_column='StokTarihi', auto_now=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stok'
        verbose_name_plural = 'Stok'

    def __str__(self):
        return "Son Guncellenme Tarihi: " + str(self.stoktarihi)


class Surushatirlat(models.Model):
    tarih = models.DateField(db_column='Tarih')  # Field name made lowercase.
    surusadi = models.CharField(db_column='SurusAdi', max_length=100)  # Field name made lowercase.
    rota = models.CharField(db_column='Rota', max_length=1000)  # Field name made lowercase.
    ortkm = models.IntegerField(db_column='OrtKm')  # Field name made lowercase.
    yapildimi = models.CharField(db_column='YapildiMi', max_length=5)  # Field name made lowercase.
    aciklama = models.CharField(db_column='Aciklama', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SurusHatirlat'
        verbose_name_plural = 'Planlanan Surusler'

    def __str__(self):
        return self.surusadi + " " + str(self.tarih)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Images(models.Model):
    ehliyetno = models.IntegerField(db_column='EhliyetNo')  # Field name made lowercase.
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'images'
        verbose_name_plural = 'Ehliyet Fotograflari'

    def __str__(self):
        return "Ehliyet No:" + str(self.ehliyetno)
