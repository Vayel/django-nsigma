from django.contrib import admin

from . import document
from .. import models


class BankDocumentAdmin(document.ModelAdmin):
    pass


admin.site.register(models.BankDocument, BankDocumentAdmin)
