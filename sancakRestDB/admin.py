from django.contrib import admin
from django.db.models import Sum

from .forms import KmTakipForm, KunyeForm, SaymanForm, PatchYelekForm, ImageForm, DisiplinForm, KasaBorcForm
from .models import Deviraldigim, Disiplin, Kunye, Giris, Etkinliksurus, Harcamalar, Kasaborc, Kmtakip, \
    Meclis, Pachyelek, Sayman, Stok, Surushatirlat, Girislog, Images, MemberLogs


@admin.register(Deviraldigim)
class DeviraldigimAdmin(admin.ModelAdmin):
    pass


@admin.register(Disiplin)
class DisiplinAdmin(admin.ModelAdmin):
    list_display = ("adisoyadi", "tarih", "uyariraporu")
    search_fields = ["adisoyadi", "uyariraporu"]
    form = DisiplinForm


@admin.register(Etkinliksurus)
class EtkinlikAdmin(admin.ModelAdmin):
    list_display = ("etkinliktarihi", "etkinlikadi", "aciklama", "etkinlikyapildimi")
    search_fields = ["etkinlikadi"]


@admin.register(Giris)
class GirisAdmin(admin.ModelAdmin):
    pass


@admin.register(Girislog)
class GirisKayitlariAdmin(admin.ModelAdmin):
    pass


@admin.register(Harcamalar)
class HarcamalarAdmin(admin.ModelAdmin):
    list_display = ("harcamayapan", "nedenharcandi", "harcanantutar")
    search_fields = ["harcamayapan", "nedenharcandi"]


@admin.register(Kasaborc)
class KasaborcAdmin(admin.ModelAdmin):
    search_fields = ["adisoyadi"]
    form = KasaBorcForm
    list_display = ("adisoyadi", "alinantutar", "alinmasebebi")


@admin.register(Kmtakip)
class KmtakipAdmin(admin.ModelAdmin):
    search_fields = ["adisoyadi"]
    list_display = ("adisoyadi", "km", "rotaturu")
    form = KmTakipForm


@admin.register(Kunye)
class KunyeAdmin(admin.ModelAdmin):
    list_display = ("nick", "adisoyadi", "plaka", "toplam_km")
    search_fields = ["adisoyadi", "nick", "plaka"]
    form = KunyeForm
    readonly_fields = ["toplam_km", "borc"]

    def toplam_km(self, obj: Kunye):
        if obj.pozisyon in ["ÇAYLAK", "CAYLAK", "ÇIRAK"]:
            toplam = Kmtakip.objects.filter(ehliyetno=obj.ehliyetno).aggregate(Sum("km"))
            return int(toplam["km__sum"])
        return obj.pozisyon

    def borc(self, obj: Kunye):
        borc = Sayman.objects.filter(ehliyetno=obj.ehliyetno,
                                     odemesekli__contains="ODENMEDI").aggregate(Sum("odenentl"))['odenentl__sum']
        return borc if borc and borc > 0 else "Karizması bulunmamaktadır."

    def get_queryset(self, request):
        qs = super(KunyeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.exclude(pozisyon__in=["EMEKLI", "AYRILDI", "BADOUT"])

    toplam_km.short_description = "Toplam KM"


@admin.register(Meclis)
class MeclisAdmin(admin.ModelAdmin):
    list_display = ("tarih", "konu", "alinankarar", "aciklama")
    search_fields = ["konu", "alinankarar", "aciklama"]


@admin.register(Pachyelek)
class PachyelekAdmin(admin.ModelAdmin):
    form = PatchYelekForm
    list_display = ("adisoyadi", "verilmetarihi")
    search_fields = ["adisoyadi"]


@admin.register(Sayman)
class SaymanAdmin(admin.ModelAdmin):
    form = SaymanForm
    list_display = ("adisoyadi", "odemetarihi", "odemesekli", "odenentl")
    search_fields = ["adisoyadi"]


@admin.register(Stok)
class StokAdmin(admin.ModelAdmin):
    pass


@admin.register(Surushatirlat)
class StokAdmin(admin.ModelAdmin):
    list_display = ("tarih", "surusadi", "rota", "ortkm")
    search_fields = ["surusadi", "rota"]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    form = ImageForm
    list_display = ("ehliyetno", "image_tag")


@admin.register(MemberLogs)
class MemberLogsAdmin(admin.ModelAdmin):
    list_display = ['action', 'username', 'ip', 'log_date']
    list_filter = ['action']
    readonly_fields = ['log_date']
