import requests
from django.test import TestCase
from django.contrib.auth.models import User


from ledger.models import Transaction


class TheTestClass(TestCase):
    def setUp(self):
        self._base_url = "http://127.0.0.1:8000/ledger/transaction/"
        self._valid_trans1 = "2015-01-16,john,mary,125.00"
        self._valid_trans2 = "2015-01-17,john,supermarket,20.00"
        self._valid_trans3 = "2015-01-17,mary,insurance,100.00"
        self._invalid_date_trans = "01/01/2012,john,mary,50"
        self._invalid_neg_amount_trans = "2015-01-17,mary,insurance,-100.00"
        self._invalid_amount_trans = "2015-01-17,mary,insurance,thousand"

    def test_process_valid_transaction(self):
        url = f"{self._base_url}process/"

        payload = {"transaction": self._valid_trans1}
        response = requests.post(url, json=payload)    
        self.assertEqual(response.status_code, 200)

        payload = {"transaction": self._valid_trans2}
        response = requests.post(url, json=payload)    
        self.assertEqual(response.status_code, 200)

        payload = {"transaction": self._valid_trans3}
        response = requests.post(url, json=payload)    
        self.assertEqual(response.status_code, 200)

        # After 3 transactions lets see whats the total
        url = f"{self._base_url}john/2021-11-11"
        john_data = requests.get(url).json()
        
        assert john_data['username'] == "john"
        assert john_data['amount'] == float(-145)

        # If we move up the date only one transaction should count
        url = f"{self._base_url}john/2015-01-16"
        john_data = requests.get(url).json()
        assert john_data['amount'] == float(-125)

    def test_process_invalid_date_transaction(self):
        url = f"{self._base_url}process/"

        payload = {"transaction": self._invalid_date_trans}
        response = requests.post(url, json=payload)    
        data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["message"], "Incorrect date format")


    def test_process_invalid_negative_amount_transaction(self):
        url = f"{self._base_url}process/"

        payload = {"transaction": self._invalid_neg_amount_trans}
        response = requests.post(url, json=payload)    
        data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["message"], "Amount should be positive")

    def test_process_invalid_negative_amount_transaction(self):
        url = f"{self._base_url}process/"

        payload = {"transaction": self._invalid_amount_trans}
        response = requests.post(url, json=payload)    
        data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["message"], "Incorrect amount format")
          
    