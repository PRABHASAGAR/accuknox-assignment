import time
import threading

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Employee


@receiver(post_save, sender=Employee)
def employee_signal(sender, instance, **kwargs):
    print("Signal Started")

    print("Signal Thread ID:", threading.get_ident())

    time.sleep(5)

    print("Signal Finished")