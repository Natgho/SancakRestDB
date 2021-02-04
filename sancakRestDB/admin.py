from django.contrib import admin

from .forms import KmTakipForm, KunyeForm, SaymanForm
from .models import Deviraldigim, Disiplin, Kunye, Giris, Etkinliksurus, Harcamalar, Kasaborc, Kmtakip, \
    Meclis, Pachyelek, Sayman, Stok, Surushatirlat, Girislog


@admin.register(Deviraldigim)
class DeviraldigimAdmin(admin.ModelAdmin):
    pass


@admin.register(Disiplin)
class DisiplinAdmin(admin.ModelAdmin):
    list_display = ("adisoyadi", "tarih", "uyariraporu")

    def get_queryset(self, request):
        qs = super(DisiplinAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(ehliyetno=int(request.user.username))


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
    pass


@admin.register(Kasaborc)
class KasaborcAdmin(admin.ModelAdmin):
    pass


@admin.register(Kmtakip)
class KmtakipAdmin(admin.ModelAdmin):
    list_display = ("adisoyadi", "km", "rotaturu")
    form = KmTakipForm

    def get_queryset(self, request):
        qs = super(KmtakipAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(ehliyetno=request.user.username)


@admin.register(Kunye)
class KunyeAdmin(admin.ModelAdmin):
    list_display = ("nick", "adisoyadi", "plaka")
    form = KunyeForm

    def get_queryset(self, request):
        qs = super(KunyeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(ehliyetno=request.user.username)


@admin.register(Meclis)
class MeclisAdmin(admin.ModelAdmin):
    list_display = ("tarih", "konu", "alinankarar", "aciklama")


@admin.register(Pachyelek)
class PachyelekAdmin(admin.ModelAdmin):
    pass


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
