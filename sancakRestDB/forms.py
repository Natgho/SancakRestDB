from datetime import date

from django.forms import ModelForm
from django import forms

from .models import Kmtakip, Kunye
from django.contrib.admin.widgets import AdminDateWidget


class KmTakipForm(ModelForm):
    adisoyadi = forms.ModelChoiceField(
        queryset=Kunye.objects.filter(pozisyon__in=["ÇAYLAK", "CAYLAK", "ÇIRAK"]).only('adisoyadi'),
        empty_label="Secim yapin")
    tarih = forms.DateField(initial=date.today, widget=AdminDateWidget())
    rotaturu = forms.ChoiceField(choices=[("TOPLANTI KM", "TOPLANTI KM"),
                                          ("ETKINLIK KM", "ETKINLIK KM")])

    def save(self, commit=True):
        instance: KmTakipForm = super(KmTakipForm, self).save(commit=False)
        instance.ehliyetno = Kunye.objects.get(adisoyadi=instance.adisoyadi).ehliyetno
        instance.km = float(instance.km) * 1.2 if instance.rotaturu == "TOPLANTI KM" else float(instance.km) * 1.5
        instance.rota = "" if not instance.rota else instance.rota
        instance.aciklama = "" if not instance.aciklama else instance.aciklama
        instance.save()
        self.save_m2m()
        return instance

    class Meta:
        model = Kmtakip
        fields = "__all__"
        exclude = ["ehliyetno"]


class KunyeForm(ModelForm):
    pozisyon = forms.ChoiceField(choices=[("ÇAYLAK", "ÇAYLAK"),
                                          ("ÇIRAK", "ÇIRAK")])
    kangrubu = forms.ChoiceField(choices=[('AB+', 'AB+'),
                                          ('AB-', 'AB-'),
                                          ('A+', 'A+'),
                                          ('A-', 'A-'),
                                          ('B+', 'B+'),
                                          ('B-', 'B-'),
                                          ('O+', 'O+'),
                                          ('O-', 'O-'), ])

    def save(self, commit=True):
        instance: Kunye = super(KunyeForm, self).save(commit=False)
        instance.yelekdontarihi = "" if not instance.yelekdontarihi else instance.yelekdontarihi
        instance.save()
        self.save_m2m()
        return instance

    class Meta:
        model = Kunye
        fields = "__all__"
