from django.contrib import admin
from django.db.models import Sum

from .forms import KmTakipForm, KunyeForm, SaymanForm, PatchYelekForm, ImageForm, DisiplinForm, KasaBorcForm
from .models import Deviraldigim, Disiplin, Kunye, Giris, Etkinliksurus, Harcamalar, Kasaborc, Kmtakip, \
    Meclis, Pachyelek, Sayman, Stok, Surushatirlat, Girislog, Images


@admin.register(Deviraldigim)
class DeviraldigimAdmin(admin.ModelAdmin):
    pass


class BaseClubModelAdmin(admin.ModelAdmin):
    restricted_members = ["ÇAYLAK", "CAYLAK", "ÇIRAK"]

    def get_queryset(self, request):
        qs = super(BaseClubModelAdmin, self).get_queryset(request)
        if request.user.is_superuser or \
                Kunye.objects.get(ehliyetno=request.user.username).pozisyon not in self.restricted_members:
            return qs
        return qs.filter(ehliyetno=int(request.user.username))


@admin.register(Disiplin)
class DisiplinAdmin(BaseClubModelAdmin):
    list_display = ("adisoyadi", "tarih", "uyariraporu")
    form = DisiplinForm


@admin.register(Etkinliksurus)
class EtkinlikAdmin(admin.ModelAdmin):
    list_display = ("etkinliktarihi", "etkinlikadi", "aciklama", "etkinlikyapildimi")


@admin.register(Giris)
class GirisAdmin(admin.ModelAdmin):
    pass


@admin.register(Girislog)
class GirisKayitlariAdmin(admin.ModelAdmin):
    pass


@admin.register(Harcamalar)
class HarcamalarAdmin(admin.ModelAdmin):
    list_display = ("harcamayapan", "nedenharcandi", "harcanantutar")


@admin.register(Kasaborc)
class KasaborcAdmin(admin.ModelAdmin):
    form = KasaBorcForm
    list_display = ("adisoyadi", "alinantutar", "alinmasebebi")


@admin.register(Kmtakip)
class KmtakipAdmin(BaseClubModelAdmin):
    list_display = ("adisoyadi", "km", "rotaturu")
    form = KmTakipForm


@admin.register(Kunye)
class KunyeAdmin(BaseClubModelAdmin):
    list_display = ("nick", "adisoyadi", "plaka", "toplam_km")
    form = KunyeForm
    readonly_fields = ['toplam_km']

    def toplam_km(self, obj: Kunye):
        if obj.pozisyon in ["ÇAYLAK", "CAYLAK", "ÇIRAK"]:
            toplam = Kmtakip.objects.filter(ehliyetno=obj.ehliyetno).aggregate(Sum('km'))
            return int(toplam['km__sum'])
        return "FULL PATCH"

    toplam_km.short_description = "Toplam KM"


@admin.register(Meclis)
class MeclisAdmin(admin.ModelAdmin):
    list_display = ("tarih", "konu", "alinankarar", "aciklama")


@admin.register(Pachyelek)
class PachyelekAdmin(admin.ModelAdmin):
    form = PatchYelekForm
    list_display = ("adisoyadi", "verilmetarihi")


@admin.register(Sayman)
class SaymanAdmin(admin.ModelAdmin):
    form = SaymanForm
    list_display = ("adisoyadi", "odemetarihi", "odemesekli", "odenentl")


@admin.register(Stok)
class StokAdmin(admin.ModelAdmin):
    pass


@admin.register(Surushatirlat)
class StokAdmin(admin.ModelAdmin):
    list_display = ("tarih", "surusadi", "rota", "ortkm")


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    form = ImageForm
    list_display = ('ehliyetno', 'image_tag')
