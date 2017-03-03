from django.contrib import admin

from daterange_filter.filter import DateRangeFilter

from .. import models, forms


class RegistrationAdmin(admin.ModelAdmin):
    filter_horizontal = ['documents']
    form = forms.Registration
    list_display = ('member', 'date', 'foreigner', 'validated',)
    list_filter = ('foreigner', 'validated', ('date', DateRangeFilter),)
    search_fields = ('member__user__username', 'member__user__first_name',
                     'member__user__last_name',)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(models.Registration, RegistrationAdmin)
