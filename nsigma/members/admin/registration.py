from django.contrib import admin

from daterange_filter.filter import DateRangeFilter
from inline_actions.admin import InlineActionsModelAdminMixin

from . import tools
from .. import models


class RegistrationAdmin(InlineActionsModelAdminMixin, admin.ModelAdmin):
    list_display = ('member', 'date', 'foreigner', 'validated',)
    list_filter = ('foreigner', 'validated', ('date', DateRangeFilter),)
    search_fields = ('member__user__username', 'member__user__first_name',
                     'member__user__last_name',)
    date_hierarchy = 'date'
    inline_actions = ['renew',]

    def has_delete_permission(self, request, obj=None):
        return False

    def renew(self, request, obj, parent_obj=None):
        params = {
            'member': obj.member.pk,
        }
        if obj.foreigner:
            params['foreigner'] = 'true'

        return tools.redirect_add_action(obj, models.Registration, params)


admin.site.register(models.Registration, RegistrationAdmin)
