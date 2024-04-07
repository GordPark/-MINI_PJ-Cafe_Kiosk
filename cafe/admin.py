from django.contrib import admin
from cafe.models import *
# Register your models here.


    
class MenuInline(admin.TabularInline):
    model = Menu
    extra = 3
    




class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Category", {"fields":["category"]}),        
    ]
    inlines = [MenuInline]
    search_fields = ["category"]

admin.site.register(Menu_Category, CategoryAdmin)