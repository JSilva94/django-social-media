from django.contrib import admin

# Register your models here.
from .models import Group, GroupMember

class GroupMemberinline(admin.TabularInline):
    model = GroupMember

admin.site.register(Group)