from django.contrib import admin

from daterange_filter.filter import DateRangeFilter

from .. import models, forms


class RegistrationDocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'member', 'created_date', 'last_update_date', 'is_in_registration',)
    list_filter = (('created_date', DateRangeFilter),)
    search_fields = ('member__user__username', 'member__user__first_name',
                     'member__user__last_name', 'name',)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(models.RegistrationDocument, RegistrationDocumentAdmin)
