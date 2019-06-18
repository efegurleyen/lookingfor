from django.contrib import admin

from .models import Product,Comment

# Register your models here.
admin.site.register(Comment)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Product
