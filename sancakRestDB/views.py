from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from sancakRestDB.models import Kunye
from sancakRestDB.utils import get_member_details


def index(request):
    return render(request, 'home.html')


@login_required
def index(request):
    context = {
        "member": get_member_details(request.user.username)
    }
    return render(request, 'home.html', context=context)


@login_required
def members(request):
    context = {
        "members": list(
            Kunye.objects.values("adisoyadi", "ehliyetno").exclude(pozisyon__in=["EMEKLI", "AYRILDI", "BADOUT"]))
    }
    return render(request, 'members.html', context=context)


@login_required
def member_info(request, ehliyetno):
    context = {
        "member": get_member_details(ehliyetno)
    }
    return render(request, 'member_info.html', context=context)


def sign_up(request):
    return render(request, 'registration/sign_up.html')
