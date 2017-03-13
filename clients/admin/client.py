from django.contrib import admin

from .. import models


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'email', 'phone_number',)
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

    last_name.admin_order_field = 'user__last_name'
    first_name.admin_order_field = 'user__first_name'
    company.admin_order_field = 'company__name'
    email.admin_order_field = 'user__email'


admin.site.register(models.Client, ClientAdmin)
