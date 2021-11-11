from datetime import datetime
from typing import Dict, Optional, Tuple

from django.contrib.auth.models import User
from rest_framework import status

from ledger.models import Transaction


class TransactionClient:
    """
    A Class to process Transaction Data

    Handle both data retrieval and incoming transactions 
    """

    def __init__(self) -> None:
        pass

    def get_user_transactions_to_date(self, username: str, date: str) -> Tuple:
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        except Exception:
            data = {"message": "incorrect date format"}
            return status.HTTP_400_BAD_REQUEST, data

        user = User.objects.filter(username=username).first()
        if not user:
            data = {"message": "User not found"}
            return status.HTTP_400_BAD_REQUEST, data

        incoming = Transaction.objects.filter(to_user=user, date__lte=date).values_list("amount", flat=True)
        outgoing = Transaction.objects.filter(from_user=user, date__lte=date).values_list("amount", flat=True)

        total_in = 0
        total_out = 0

        for value in incoming:
            total_in += value

        for value in outgoing:
            total_out += value

        amount_to_date = total_in - total_out
        data = { "username": user.username, "amount": amount_to_date}

        return status.HTTP_200_OK, data


    def process_user_transaction(self, transaction_data) -> Tuple:
        """
            2015-01-16,john,mary,125.00 (data example)
        """

        date, user_from, user_to, amount = transaction_data["transaction"].split(",")

        try:
            validated_date = datetime.strptime(date, '%Y-%m-%d').date()
        except Exception:
            data = {"message": "incorrect date format"}
            return status.HTTP_400_BAD_REQUEST, data

        # To keep it simple lets accept John == john and .lower() everything
 
        user_from = user_from.lower()
        user_to = user_to.lower()

        if user_from == user_to:
            data = {"message": "Users must be different"}
            return status.HTTP_400_BAD_REQUEST, data

        try:
            validated_amount = float(amount)
        except ValueError:
            data = {"message": "incorrect amount format"}
            return status.HTTP_400_BAD_REQUEST, data

        # If the user does not exists lets create one
        try:
            from_user = User.objects.get(username=user_from)
        except User.DoesNotExist:
            from_user = User(username=user_from)
            from_user.save()

        try:
            to_user = User.objects.get(username=user_to)
        except User.DoesNotExist:
            to_user = User(username=user_to)
            to_user.save()

        #Everything ok, lets save the transaction
        tran = Transaction(date=validated_date, from_user=from_user, to_user=to_user, amount=validated_amount)
        tran.save()
        data = {"message": "Transaction sucessfull"}
        return status.HTTP_200_OK, data