from django.contrib import admin
from django.utils.html import format_html

from transactions.models import Recurring, Transaction


@admin.register(Recurring)
class RecurringAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', '_amount', '_type', 'until', 'repeat', )
    list_filter = ('until', 'repeat', 'is_active', )
    search_fields = ('user__email', 'user__first_name',  'user__last_name', 'description', )
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    readonly_fields = ('created_at', 'updated_at', )

    fieldsets = (
        ('Transaction', {'fields': ('transaction', )}),
        ('Recurring', {'fields': ('is_active', 'until', 'repeat',)}),
        ('Debug', {'fields': ('created_at', 'updated_at')}),
    )

    def _amount(self, obj):
        return format_html(f"<b style='color:{'green' if obj.transaction.is_revenue else 'red'};'>{obj.transaction.amount}</b>")

    def _type(self, obj):
        return (obj.transaction.revenue_type if obj.transaction.is_revenue else obj.transaction.expenses_type) if obj.transaction.revenue_type or obj.transaction.expenses_type else '-'


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', '_amount', '_type', 'description', )
    list_filter = ('is_revenue', 'revenue_type', 'expenses_type', )
    search_fields = ('user__email', 'user__first_name',  'user__last_name', 'revenue_type', 'expenses_type', 'amount', 'description', )
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    readonly_fields = ('created_at', 'updated_at', )

    fieldsets = (
        ('Transaction', {'fields': ('user', 'amount', 'is_revenue', 'revenue_type', 'expenses_type', 'description', )}),
        ('Debug', {'fields': ('created_at', 'updated_at')}),
    )

    def _amount(self, obj):
        return format_html(f"<b style='color:{'green' if obj.is_revenue else 'red'};'>{obj.amount}</b>")

    def _type(self, obj):
        return (obj.revenue_type if obj.is_revenue else obj.expenses_type) if obj.revenue_type or obj.expenses_type else '-'
