from django.contrib import admin

from daterange_filter.filter import DateRangeFilter
from inline_actions.admin import InlineActionsModelAdminMixin

from . import tools
from .. import models


class RegistrationDocumentAdmin(InlineActionsModelAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'member', 'created_date', 'last_update_date', 'is_in_registration',)
    list_filter = (('created_date', DateRangeFilter),)
    search_fields = ('member__user__username', 'member__user__first_name',
                     'member__user__last_name', 'name',)
    raw_id_fields = ('member',)
    inline_actions = ['renew',]

    def has_delete_permission(self, request, obj=None):
        return False

    def renew(self, request, obj, parent_obj=None):
        params = {
            'member': obj.member.pk,
            'name': obj.name,
        }

        return tools.redirect_add_action(obj, models.RegistrationDocument, params)


admin.site.register(models.RegistrationDocument, RegistrationDocumentAdmin)
