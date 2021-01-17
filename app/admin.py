from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=Profile):
        return False
    def has_add_permission(self, request, obj=Profile):
        profile = Profile.objects.all()
        if len(profile) == 1:
            return False

    list_display = [
        'first_name',
        'last_name',
        'age',
        'email',
        'phone',
    ]


class PortfolioAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'cat',
        'date',
    ]
    search_fields = ['title','cat']

class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=Profile):
        return False
    list_display = [
        'name',
        'sub',
        'date'
    ]
    search_fields = ['name','sum']






admin.site.register(Profile, ProfileAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Contact, ContactAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)

###############################
admin.site.site_header = ' لوحة التحكم'
admin.site.site_title = 'mhmd.y'
admin.site.index_title = 'mhmd.y'
