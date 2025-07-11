from django.contrib import admin
from .models import Wallet, Transaction

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'currency', 'last_updated')
    search_fields = ('user__email',)
    list_filter = ('currency',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'txn_type', 'amount', 'reference', 'timestamp')
    search_fields = ('reference', 'wallet__user__email')
    list_filter = ('txn_type', 'timestamp')
