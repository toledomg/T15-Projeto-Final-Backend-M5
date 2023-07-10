from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


class LoansConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "loans"

    def ready(self):
        from .scheduler import LoanSchedulerJob, Loan2SchedulerJob

        scheduler.add_job(
            LoanSchedulerJob.run,
            trigger="interval",
            seconds=3,
            id="check_devolution",
            replace_existing=True,
        )
        scheduler.add_job(
            Loan2SchedulerJob.run,
            trigger="interval",
            seconds=3,
            id="check_devolution",
            replace_existing=True,
        )

        scheduler.start()
