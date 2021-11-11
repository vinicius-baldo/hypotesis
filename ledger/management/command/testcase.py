from django.core.management.base import BaseCommand
import requests

from django.contrib.auth.models import User
from ledger.models import Transaction


class Command(BaseCommand):
    def handle(self, **options):

        test_data = "2015-01-16,john,mary,125.00"
        url = 'http://127.0.0.1:8000/ledger/transaction/process/'
        payload = {"transaction": test_data}
        response = requests.post(url, json=payload)

        assert response.status_code == 200
        