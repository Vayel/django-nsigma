from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from inline_actions.admin import InlineActionsModelAdminMixin

from . import tools as admin_tools
from .. import models
from .. import tools


class WasRegisteredListFilter(admin.SimpleListFilter):
    title = _('was registered')
    parameter_name = 'was_registered'

    THIS_YEAR = 'this_year'
    LAST_YEAR = 'last_year'
    THIS_MANDATE = 'this_mandate'

    def lookups(self, request, model_admin):
        return (
            ('this_year', _('This year')),
            ('last_year', _('Last year')),
            ('this_mandate', _('This mandate')),
        )

    def queryset(self, request, queryset):
        if self.value() == self.THIS_YEAR:
            ldate, hdate = tools.dates.registration_year_range()
        if self.value() == self.LAST_YEAR:
            ldate, hdate = tools.dates.registration_year_range(year_delta=-1)
        if self.value() == self.THIS_MANDATE:
            ldate, _ = tools.dates.registration_year_range(year_delta=-1)
            _, hdate = tools.dates.registration_year_range()

        if self.value() in (self.THIS_YEAR, self.LAST_YEAR, self.THIS_MANDATE,):
            return queryset.filter(
                registrations__date__gte=ldate,
                registrations__date__lte=hdate,
            )


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
    list_filter = (WasRegisteredListFilter,)
    search_fields = ('user__username', 'user__first_name', 'user__last_name',
                     'user__email',)
    ordering = ('user__last_name', 'user__first_name',)
    inline_actions = ['register', 'add_document',]
    inlines = [RegistrationInline, DocumentInline,]

    def username(self, obj):
        return obj.user.username

    def last_name(self, obj):
        return obj.user.last_name

    def first_name(self, obj):
        return obj.user.first_name

    def email(self, obj):
        return obj.user.email

    def last_registration_date(self, obj):
        reg = obj.last_registration
        return reg.date if reg is not None else None

    username.admin_order_field = 'user__username'
    last_name.admin_order_field = 'user__last_name'
    first_name.admin_order_field = 'user__first_name'
    email.admin_order_field = 'user__email'
    last_registration_date.admin_order_field = 'last_registration_date'

    def has_delete_permission(self, request, obj=None):
        return False

    def register(self, request, obj, parent_obj=None):
        params = {
            'member': obj.pk,
        }
        if obj.last_registration.foreigner:
            params['foreigner'] = 'true'

        return admin_tools.redirect_add_action(obj, models.Registration, params)

    def add_document(self, request, obj, parent_obj=None):
        params = {
            'member': obj.pk,
        }
        return admin_tools.redirect_add_action(obj, models.RegistrationDocument, params)


admin.site.register(models.Member, MemberAdmin)
