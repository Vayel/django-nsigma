from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .. import models


class IsAlumniListFilter(admin.SimpleListFilter):
    title = _('alumni')
    parameter_name = 'alumni'

    def lookups(self, request, model_admin):
        return (
            ('yes', _('Yes')),
            ('no', _('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'no':
            return queryset.filter(alumni=False)
        elif self.value() == 'yes':
            return queryset.filter(alumni=True)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'email',
                    'phone_number', 'alumni',)
    list_filter = (IsAlumniListFilter,)
    search_fields = ('user__first_name', 'user__last_name', 'company__name',)
    raw_id_fields = ('user', 'company',) 

    def last_name(self, obj):
        return obj.user.last_name

    def first_name(self, obj):
        return obj.user.first_name

    def company(self, obj):
        return obj.company.name

    def email(self, obj):
        return obj.user.email

    def alumni(self, obj):
        return obj.alumni

    last_name.admin_order_field = 'user__last_name'
    first_name.admin_order_field = 'user__first_name'
    company.admin_order_field = 'company__name'
    email.admin_order_field = 'user__email'
    alumni.admin_order_field = 'alumni'
    alumni.boolean = True


admin.site.register(models.Client, ClientAdmin)
