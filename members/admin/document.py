from django.contrib import admin

from daterange_filter.filter import DateRangeFilter


class Inline(admin.TabularInline):
    extra = 0
    ordering = ['-created_date', 'name',]
    readonly_fields = ['created_date', 'last_update_date',]


class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'member', 'created_date', 'last_update_date',)
    list_filter = (('created_date', DateRangeFilter),)
    search_fields = ('member__user__username', 'member__user__first_name',
                     'member__user__last_name', 'name',)
    raw_id_fields = ('member',)

    def has_delete_permission(self, request, obj=None):
        return False

