from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
   
    search_fields = ['first_name', 'last_name', 'email'] 
    list_filter = ['is_active', 'is_staff'] 
    ordering = ['last_name', 'first_name'] 
    list_display = ['first_name', 'last_name', 'email', 'is_active', 'is_staff'] 
    
admin.site.register(CustomUser, CustomUserAdmin)
