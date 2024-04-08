from django.contrib import admin

from app.models import Client, ChineseStorage, UzbekStorage, Party

# Register your models here.#


admin.site.register([Client,
                     Party,
                     ChineseStorage,
                     UzbekStorage])
