
from django.urls import path
from .views import test_sync, test_thread, test_transaction

urlpatterns = [
    path("sync/", test_sync, name="sync"),
    path("thread/", test_thread, name="thread"),
    path("transaction/", test_transaction, name="transaction"),
]