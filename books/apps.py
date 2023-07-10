from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
import time

scheduler = BackgroundScheduler()

class BooksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "books"

    def ready(self):
        from .scheduler import BookSchedulerJob

        scheduler.add_job(
            BookSchedulerJob.run,
            trigger="interval",
            seconds=6,
            # horas=24,
            id="check_send_mail",
            replace_existing=True,
        )

        # scheduler.start()