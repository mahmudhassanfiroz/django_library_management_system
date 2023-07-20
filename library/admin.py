# library/admin.py

from django.contrib import admin
from .models import Book, Reservation
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Define an inline for the User model to show additional fields in the admin panel
class UserInline(admin.StackedInline):
    model = User
    can_delete = False
    verbose_name_plural = 'Profile'

# Define a new UserAdmin class
class UserAdmin(BaseUserAdmin):
    inlines = (UserInline,)

# Re-register User model with the new UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register Book and Reservation models
admin.site.register(Book)
admin.site.register(Reservation)
