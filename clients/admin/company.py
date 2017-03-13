from django.contrib import admin

from .. import models


class ClientInline(admin.TabularInline):
    model = models.Client
    extra = 0
    raw_id_fields = ('user',) 


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'sector', 'type', 'site_link', 'origin',)
    list_filter = ('sector', 'type', 'origin',)
    search_fields = ('name',)
    inlines = (ClientInline,)

admin.site.register(models.Company, CompanyAdmin)
