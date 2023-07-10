from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.job import Job

from users.models import User
from datetime import date, datetime
from django.utils import timezone
from django.utils.timezone import make_aware

from django.contrib.auth import get_user_model

user = get_user_model


def block_user(pk):
    user = User.objects.get(pk=pk)
    user.is_allowed = False
    user.save()


class LoanSchedulerJob(Job):
    @staticmethod
    def run():
        from .models import Loans

        data_atual = make_aware(datetime.now())

        loans = Loans.objects.all()   
        # if not loans.is_returned and loans.blocking_date > timezone.now():

        for loan in loans:

            print(loan.user.id)

            if not loan.is_returned and loan.blocking_date is not None and loan.blocking_date < timezone.now():
                block_user(loan.user.id)

                loan.save()        

