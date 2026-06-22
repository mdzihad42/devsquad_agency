from django.contrib import admin
from .models import VisitorCount, Transaction, SEOData

@admin.register(VisitorCount)
class VisitorCountAdmin(admin.ModelAdmin):
    list_display = ('page_path', 'count', 'last_visit')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'transaction_type', 'category', 'date')
    list_filter = ('transaction_type', 'category', 'date')

@admin.register(SEOData)
class SEODataAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'title_tag')
