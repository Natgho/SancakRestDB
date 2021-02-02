from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

app_models = apps.get_app_config('sancakRestDB').get_models()
for model in app_models:
    try:
        if not model._meta.db_table.startswith("auth") and not model._meta.db_table.startswith("django"):
            admin.site.register(model)
    except AlreadyRegistered:
        pass
# Register your models here.
# TODO add all models here.
