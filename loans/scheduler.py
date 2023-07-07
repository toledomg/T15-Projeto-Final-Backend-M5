from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.job import Job

from datetime import date, datetime
from django.utils import timezone


from django.contrib.auth import get_user_model

user = get_user_model

def block_user(pk):
    user = user.objects.get(pk=pk)
    user.is_allowed = False
    user.save()
    print(user)



class LoanSchedulerJob(Job):
    @staticmethod
    def init_scheduler():
        from .models import Loans

        loans = Loans.objects.filter(is_returned=False, loan_return=timezone.now())
        for loan in loans:
            block_user(loan.user_id)
            loan.save    
          