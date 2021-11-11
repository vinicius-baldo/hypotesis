import requests
from django.test import TestCase
from django.contrib.auth.models import User


from ledger.models import Transaction


class TheTestClass(TestCase):
    def setUp(self):
        self._base_url = "http://127.0.0.1:8000/ledger/transaction/"
        self._trans1 = "2015-01-16,john,mary,125.00"
        self._trans2 = "2015-01-17,john,supermarket,20.00"
        self._trans3 = "2015-01-17,mary,insurance,100.00"


    def test_process_transaction(self):

        # Lets clear the transaction database
        # On a production env this is not required 
        # But here we cant lets olders tests interfere

        # trans = Transaction.objects.all()
        # trans.delete()

        url = f"{self._base_url}process/"

        payload = {"transaction": self._trans1}
        response = requests.post(url, json=payload)    
        assert response.status_code == 200

        payload = {"transaction": self._trans2}
        response = requests.post(url, json=payload)    
        assert response.status_code == 200

        payload = {"transaction": self._trans3}
        response = requests.post(url, json=payload)    
        assert response.status_code == 200

        # After 3 transactions lets see whats the total
        url = f"{self._base_url}john/2021-11-11"
        john_data = requests.get(url).json()
        
        assert john_data['username'] == "john"
        assert john_data['amount'] == float(-145)

        # Lets check if we move up the date
        url = f"{self._base_url}john/2015-01-16"
        john_data = requests.get(url).json()
        assert john_data['amount'] == float(-125)