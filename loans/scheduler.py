from apscheduler.job import Job

from users.models import User

from datetime import datetime
from django.utils.timezone import make_aware

user = User.objects.all()


def block_user(pk):
    user = User.objects.get(id=pk)
    user.is_allowed = False
    user.save()


def unblock_user(pk):
    user = User.objects.get(id=pk)
    user.is_allowed = True
    user.save()


class LoanSchedulerJob(Job):
    @staticmethod
    def run():
        from .models import Loans
        from users.models import User

        data_atual = make_aware(datetime.now())

        loans = Loans.objects.all()

        for loan in loans:
            if not loan.is_returned and loan.loan_return < data_atual:
                block_user(loan.user.id)
                loan.save()


class Loan2SchedulerJob(Job):
    @staticmethod
    def run():
        from .models import Loans
        from users.models import User

        data_atual = make_aware(datetime.now())

        loans = Loans.objects.all()

        for loan in loans:
            if loan.is_returned and loan.blocking_date <= data_atual:
                unblock_user(loan.user.id)
                loan.save()
