from datetime import timedelta, timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Wallet, Transaction
from .serializers import WalletBalanceSerializer, TopUpSerializer, TransactionSerializer
from django.db import transaction as db_transaction
from django.db.models import F
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

"""
API endpoint to retrieve the authenticated user's wallet balance.
This endpoint returns the user's wallet balance and currency.
"""
class WalletBalanceView(APIView):
    permission_classes = [IsAuthenticated]
    @method_decorator(ratelimit(key='ip', rate='5/m', method='POST', block=True))
    def get(self, request):
        user = request.user
        try:
            wallet = Wallet.objects.get(user=user)
        except Wallet.DoesNotExist:
            return Response({"error": "Wallet not found"}, status=404)

        serializer = WalletBalanceSerializer(wallet)
        return Response(serializer.data, status=200)

"""
API endpoint to retrieve a specific transaction by reference.
This endpoint returns the details of a transaction for the authenticated user.
"""
class TransactionDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        ref = request.query_params.get('reference')
        if not ref:
            return Response({"error": "Reference is required."}, status=400)
        try:
            transaction = Transaction.objects.get(reference=ref, wallet__user=request.user)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found."}, status=404)

        serializer = TransactionSerializer(transaction)
        return Response(serializer.data, status=200)

"""
API endpoint to retrieve all transactions for the authenticated user.
This endpoint returns a list of all transactions associated with the user's wallet.
"""
class TransactionAllDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        try:
            wallet = Wallet.objects.get(user=user)
        except Wallet.DoesNotExist:
            return Response({"error": "Wallet not found"}, status=404)

        transactions = wallet.transactions.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=200)
    
class InitiateTopUpView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = TopUpSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        amount = serializer.validated_data['amount']
        wallet = Wallet.objects.get(user=request.user)

        txn = Transaction.objects.create(
            wallet=wallet,
            txn_type=Transaction.TOP_UP,
            amount=amount,
            status=Transaction.STATUS_PENDING,
            note="User initiated top-up"
        )
        return Response({
            "message": "Top-up initiated",
            "reference": txn.reference,
            "amount": str(amount),
            "status": txn.status,
        }, status=201)

"""
API endpoint to confirm a top-up transaction.
This endpoint simulates payment verification and updates the transaction status.
It should be replaced with real payment gateway verification in production.
"""
class ConfirmTopUpView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        reference = request.data.get("reference")
        payment_verified = request.data.get("verified")  # Should be real verification!

        if not reference or payment_verified != True:
            return Response({"error": "Invalid confirmation"}, status=400)

        with db_transaction.atomic():
            try:
                txn = Transaction.objects.select_for_update().get(
                    reference=reference,
                    wallet__user=request.user
                )
            except Transaction.DoesNotExist:
                return Response({"error": "Transaction not found"}, status=404)

            if timezone.now() - txn.timestamp > timedelta(minutes=10):
                txn.status = Transaction.STATUS_EXPIRED
                txn.save(update_fields=["status"])
                return Response({
                    "error": "Transaction expired. Please initiate a new top-up."
                }, status=410)

            if txn.status == Transaction.STATUS_COMPLETED:
                return Response({"message": "Already completed"}, status=200)

            txn.status = Transaction.STATUS_COMPLETED
            txn.save(update_fields=["status"])

            wallet = txn.wallet
            wallet.balance = F('balance') + txn.amount
            wallet.save(update_fields=["balance"])
            wallet.refresh_from_db()
        return Response({
            "message": "Top-up confirmed",
            "reference": txn.reference,
            "new_balance": str(wallet.balance)
        }, status=200)