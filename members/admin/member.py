from django.contrib import admin

from inline_actions.admin import InlineActionsModelAdminMixin

from . import tools
from .. import models


class RegistrationInline(admin.TabularInline):
    model = models.Registration
    extra = 0
    ordering = ['-date']


class DocumentInline(admin.TabularInline):
    model = models.RegistrationDocument
    extra = 0
    ordering = ['-created_date', 'name',]
    readonly_fields = ['created_date', 'last_update_date',]


class MemberAdmin(InlineActionsModelAdminMixin, admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'email',
                    'last_registration_date',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name',
                     'user__email',)
    ordering = ('user__last_name', 'user__first_name',)
    inline_actions = ['register', 'add_document',]
    inlines = [RegistrationInline, DocumentInline,]

    def has_delete_permission(self, request, obj=None):
        return False

    def last_registration_date(self, obj):
        reg = obj.last_registration
        return reg.date if reg is not None else None

    def register(self, request, obj, parent_obj=None):
        params = {
            'member': obj.pk,
        }
        if obj.last_registration.foreigner:
            params['foreigner'] = 'true'

        return tools.redirect_add_action(obj, models.Registration, params)

    def add_document(self, request, obj, parent_obj=None):
        params = {
            'member': obj.pk,
        }
        return tools.redirect_add_action(obj, models.RegistrationDocument, params)


admin.site.register(models.Member, MemberAdmin)
