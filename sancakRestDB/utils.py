# Created by Sezer BOZKIR<admin@sezerbozkir.com at 2/28/2021
from django.db.models import Sum
from django.forms import model_to_dict

from sancakRestDB.models import Kunye, Kmtakip, Sayman
from datetime import datetime


def get_member_details(ehliyetno):
    member = Kunye.objects.get(ehliyetno=ehliyetno)
    member = model_to_dict(member)
    day_of_member = (datetime.now().date() - member['kgiristarihi']).days
    sum_km = Kmtakip.objects.filter(ehliyetno=ehliyetno).aggregate(Sum("km"))
    debt = Sayman.objects.filter(ehliyetno=ehliyetno,
                                 odemesekli__contains="ODENMEDI").aggregate(Sum("odenentl"))['odenentl__sum']
    member = {
        "fullname": member['adisoyadi'],
        "nick": member['nick'],
        "rank": member['pozisyon'],
        "join_date": member['kgiristarihi'],
        "date_of_oath": member['yemintarihi'],
        "motorcycle_name": f"{member['motormarka']} {member['motorcc']}",
        "plaque": member["plaka"],
        "blood_group": member['kangrubu'],
        "day_of_member": day_of_member,
        "sum_km": "FULL" if member['pozisyon'] not in ["ÇAYLAK", "ÇIRAK"] else sum_km,
        "debt": f"{debt} TL" if debt and debt > 0 else "Karizması bulunmamaktadır.",
        "relative": member['aciklama'],
        "relative_tel": member['yakintelno']
    }
    return member
