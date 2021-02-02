# Created by Sezer BOZKIR<admin@sezerbozkir.com at 2/2/2021
from rest_framework import serializers

from .models import Giris


class GirisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Giris
        fields = ('ehliyetno', 'yetki', 'gorevi')
