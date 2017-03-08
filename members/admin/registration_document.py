from django.contrib import admin

from inline_actions.admin import InlineActionsModelAdminMixin

from . import document, tools
from .. import models


class RegistrationDocumentAdmin(InlineActionsModelAdminMixin, document.ModelAdmin):
    inline_actions = ['renew',]

    def renew(self, request, obj, parent_obj=None):
        params = {
            'member': obj.member.pk,
            'name': obj.name,
        }

        return tools.redirect_add_action(obj, models.Document, params)


admin.site.register(models.RegistrationDocument, RegistrationDocumentAdmin)
