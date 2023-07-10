from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.job import Job

from datetime import date, datetime
from django.utils import timezone


from django.contrib.auth import get_user_model


User = get_user_model


def block_user(pk):
    user = User.objects.get(pk=pk)
    user.is_allowed = False
    user.save()
    print(user)


class LoanSchedulerJob(Job):
    @staticmethod
    def run():
        from .models import Loans

        loans = Loans.objects.filter(is_returned=False, blocking_date=timezone.now())
        print("deu certo")
        for loan in loans:
            block_user(loan.user_id)
            loan.save
