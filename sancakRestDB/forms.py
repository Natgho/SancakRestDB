from datetime import date

from django.forms import ModelForm
from django import forms

from .models import Kmtakip, Kunye, Sayman, Pachyelek, Images, Disiplin, Kasaborc
from django.contrib.admin.widgets import AdminDateWidget


class BaseClubForm(ModelForm):
    adisoyadi = forms.ModelChoiceField(
        queryset=Kunye.objects.all(),
        to_field_name='adisoyadi',
        empty_label="Secim yapin")

    def __init__(self, *args, **kwargs):
        instance: Kunye = kwargs.get('instance', None)
        super(BaseClubForm, self).__init__(*args, **kwargs)

        if instance:
            adisoyadi = Kunye.objects.get(ehliyetno=str(instance.ehliyetno)).adisoyadi
            self.initial['adisoyadi'] = adisoyadi


class DefaultClubForm(BaseClubForm):
    def save(self, commit=True):
        instance = super(DefaultClubForm, self).save(commit=False)
        instance.ehliyetno = Kunye.objects.get(adisoyadi=instance.adisoyadi).ehliyetno
        instance.save()
        self.save_m2m()
        return instance


class KmTakipForm(BaseClubForm):
    adisoyadi = forms.ModelChoiceField(
        queryset=Kunye.objects.filter(pozisyon__in=["ÇAYLAK", "CAYLAK", "ÇIRAK"]),
        to_field_name='adisoyadi',
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
        # TODO labels = {'dbadi':'olmasiniistediginad'}


class KunyeForm(ModelForm):
    # TODO add total debt
    pozisyon = forms.ChoiceField(choices=[("ÇAYLAK", "ÇAYLAK"),
                                          ("ÇIRAK", "ÇIRAK"),
                                          ("BASKAN", "BASKAN"),
                                          ("KORDINATÖR", "KORDINATÖR"),
                                          ("DISIPLIN", "DISIPLIN"),
                                          ("KOÇ", "KOÇ"),
                                          ("SAYMAN", "SAYMAN"),
                                          ("BAŞ YOL KAPTANI", "BAŞ YOL KAPTANI"),
                                          ("FULL", "FULL"),
                                          ])
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


class SaymanForm(BaseClubForm):
    odemetarihi = forms.DateField(initial=date.today, widget=AdminDateWidget())
    odemesekli = forms.ChoiceField(choices=[("AIDAT", "AIDAT"),
                                            ("AIDAT ODENMEDI", "AIDAT ODENMEDI"),
                                            ("DIGER ODEME", "DIGER ODEME"),
                                            ("PACH PARASI", "PACH PARASI"),
                                            ("PACH PARASI ODENMEDI", "PACH PARASI ODENMEDI"),
                                            ])

    def save(self, commit=True):
        instance: Sayman = super(SaymanForm, self).save(commit=False)
        instance.ehliyetno = Kunye.objects.get(adisoyadi=instance.adisoyadi).ehliyetno
        instance.odemeaciklama = "" if not instance.odemeaciklama else instance.odemeaciklama
        instance.aciklama = "" if not instance.aciklama else instance.aciklama
        if not instance.odenentl:
            if instance.odemesekli == "AIDAT":
                instance.odenentl = 20.0
            elif instance.odemesekli == "AIDAT ODENMEDI":
                instance.odenentl = 0.0
            elif instance.odemesekli == "PACH PARASI":
                instance.odenentl = 150.0
        instance.save()
        self.save_m2m()
        return instance

    class Meta:
        model = Sayman
        fields = "__all__"
        exclude = ["ehliyetno"]


class PatchYelekForm(BaseClubForm):
    verilmetarihi = forms.DateField(initial=date.today, widget=AdminDateWidget())
    yelek = forms.ChoiceField(choices=[("EVET", "EVET"),
                                       ("HAYIR", "HAYIR")])
    bayrak = forms.ChoiceField(choices=[("EVET", "EVET"),
                                        ("HAYIR", "HAYIR")])
    onsancak = forms.ChoiceField(choices=[("EVET", "EVET"),
                                          ("HAYIR", "HAYIR")])
    onkurukafa = forms.ChoiceField(choices=[("EVET", "EVET"),
                                            ("HAYIR", "HAYIR")])
    chopper = forms.ChoiceField(choices=[("EVET", "EVET"),
                                         ("HAYIR", "HAYIR")])
    mk = forms.ChoiceField(choices=[("EVET", "EVET"),
                                    ("HAYIR", "HAYIR")])
    bursa = forms.ChoiceField(choices=[("EVET", "EVET"),
                                       ("HAYIR", "HAYIR")])
    sirtsancak = forms.ChoiceField(choices=[("EVET", "EVET"),
                                            ("HAYIR", "HAYIR")])
    sirtkurukafa = forms.ChoiceField(choices=[("EVET", "EVET"),
                                              ("HAYIR", "HAYIR")])
    turkiye = forms.ChoiceField(choices=[("EVET", "EVET"),
                                         ("HAYIR", "HAYIR")])

    def save(self, commit=True):
        instance: Pachyelek = super(PatchYelekForm, self).save(commit=False)
        instance.ehliyetno = Kunye.objects.get(adisoyadi=instance.adisoyadi).ehliyetno
        instance.save()
        self.save_m2m()
        return instance

    class Meta:
        model = Pachyelek
        fields = "__all__"
        exclude = ["ehliyetno"]


class ImageForm(BaseClubForm):
    image_tag = forms.ImageField()

    class Meta:
        model = Images
        fields = "__all__"
        exclude = ["ehliyetno", 'image']

    def save(self, commit=True):
        instance: Images = super(ImageForm, self).save(commit=False)
        instance.ehliyetno = Kunye.objects.get(adisoyadi=instance.adisoyadi).ehliyetno
        instance.save()
        self.save_m2m()
        return instance


class DisiplinForm(DefaultClubForm):
    class Meta:
        model = Disiplin
        fields = "__all__"
        exclude = ["ehliyetno"]


class KasaBorcForm(DefaultClubForm):
    class Meta:
        model = Kasaborc
        fields = "__all__"
        exclude = ["ehliyetno"]
