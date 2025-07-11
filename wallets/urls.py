from django.urls import path
from .views import WalletBalanceView, TransactionDetailView, TransactionAllDetailView, InitiateTopUpView, ConfirmTopUpView

urlpatterns = [
    path('balance/', WalletBalanceView.as_view(), name='wallet-balance'),
    path('top-up/initiate/', InitiateTopUpView.as_view(), name='wallet-top-up'),
    path('top-up/confirm/', ConfirmTopUpView.as_view(), name='wallet-top-up'),
    path('transaction/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transaction/all/', TransactionAllDetailView.as_view(), name='transaction-detail')
]
