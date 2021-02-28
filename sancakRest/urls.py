# Created by Sezer BOZKIR<admin@sezerbozkir.com at 27/2/2021
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [url(r'^i18n/', include('django.conf.urls.i18n')), ]
urlpatterns += [
    path('admin/', admin.site.urls),
    path('', include('sancakRestDB.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
