from django.contrib import admin
from .models import Surname,Member
# Register your models here.

class SurnameAdmin(admin.ModelAdmin):
    '''
        Admin View for
    '''
    list_display = ('id','family_name')
    list_filter = ('family_name',)

    search_fields = ('family_name',)


admin.site.register(Surname,SurnameAdmin)


class MemberAdmin(admin.ModelAdmin):
    '''
        Admin View for
    '''
    list_display = ('id','persons_name','persons_dob')
    list_filter = ('persons_name','persons_dob')
    search_fields = ('persons_name',)


admin.site.register(Member,MemberAdmin)
