# Created by Sezer BOZKIR<admin@sezerbozkir.com at 2/2/2021
from django.urls import include, path

from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='home'),
    path("members", views.members, name="member_list"),
    path("members/<str:ehliyetno>", views.member_info, name="member_info"),
    path('accounts/sign_up/', views.sign_up, name="sign-up"),
]
