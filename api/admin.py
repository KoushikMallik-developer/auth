from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from api.models.user import User
from api.models.verification import Verification


# Register your models here.

class UserAdmin(UserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'fname', 'lname', 'dob', 'phone', 'is_active', 'created_at', 'updated_at', 'image',
                    'is_admin', 'username')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('id', 'email', 'password')}),
        ('Personal info', {'fields': ('username', 'fname', 'lname', 'dob', 'phone', 'image')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'fname', 'lname', 'is_active', 'is_admin',
                       'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'fname', 'phone', 'lname', 'username')
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.register(Verification)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
