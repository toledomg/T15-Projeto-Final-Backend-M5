from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()

class LoansConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "loans"

    def ready(self):
        from .scheduler import LoanSchedulerJob

        scheduler.add_job(
            LoanSchedulerJob.init_scheduler,
            trigger="interval",
            seconds=6,
            id="check_devolution",
            replace_existing=True,
        )

        scheduler.start()
