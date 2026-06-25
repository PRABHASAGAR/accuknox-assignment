import time
import threading

from django.db import transaction
from django.http import HttpResponse

from .models import Employee


def test_sync(request):
    start = time.time()

    Employee.objects.create(name="John")

    end = time.time()

    return HttpResponse(
        f"Execution Time: {end - start:.2f} seconds"
    )


def test_thread(request):
    print("View Thread ID:", threading.get_ident())

    Employee.objects.create(name="Thread Test")

    return HttpResponse("Thread Test Completed")


def test_transaction(request):
    try:

        with transaction.atomic():

            Employee.objects.create(
                name="Transaction Test"
            )

            raise Exception("Rollback Transaction")

    except Exception:
        pass

    count = Employee.objects.count()

    return HttpResponse(
        f"Employee Count: {count}"
    )


from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse
from .models import Employee


def test_transaction(request):
    before = Employee.objects.count()

    try:
        with transaction.atomic():
            Employee.objects.create(name="Transaction Test")
            raise Exception("Rollback Transaction")

    except Exception:
        pass

    after = Employee.objects.count()

    return HttpResponse(
        f"Before: {before}<br>"
        f"After: {after}"
    )
from django.db import transaction
from django.http import HttpResponse
from .models import Employee


def test_transaction(request):
    before = Employee.objects.count()

    try:
        with transaction.atomic():
            Employee.objects.create(name="Transaction Test")
            raise Exception("Rollback Transaction")

    except Exception:
        pass

    after = Employee.objects.count()

    return HttpResponse(
        f"Before: {before}<br>"
        f"After: {after}"
    )