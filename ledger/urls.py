from django.urls import path
from .views import TransactionToDate, ProcessTransaction


urlpatterns = [
    path('transaction/<str:username>/<str:date>/', TransactionToDate.as_view()),
    path('transaction/process/', ProcessTransaction.as_view()),
]
