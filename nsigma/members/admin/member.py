from django.contrib import admin

from .. import models


class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'email',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name',
                     'user__email',)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(models.Member, MemberAdmin)
