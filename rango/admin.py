from django.contrib import admin

# Register your models here.
from django.contrib import admin
from rango.models import Category, Page, UserProfile

# Category
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

# Page
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)

admin.site.register(UserProfile)
