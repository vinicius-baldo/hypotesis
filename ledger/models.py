from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.from_user} -> {self.to_user} : {self.amount}"