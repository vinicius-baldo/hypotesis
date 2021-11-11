from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from ledger.TransactionClient import TransactionClient

class TransactionToDate(APIView):
    def get(self, request, username, date, *args, **kwargs):
        """API for retrieving user transaction data up until the date."""
        response_status, response_data = TransactionClient().get_user_transactions_to_date(
            username, date
        )
        return Response(
            status=response_status,
            data=response_data,
        )

class ProcessTransaction(APIView):
    def post(self, request, *args, **kwargs):
        """API for registring a user transaction to another."""
        response_status, response_data = TransactionClient().process_user_transaction(
            request.data
        )
        
        return Response(
            status=response_status,
            data=response_data,
        )

        