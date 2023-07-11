from apscheduler.job import Job
from django.core.mail import send_mail
from .models import Follow, Book
import os


def send_emails():
    books = Book.objects.filter(copies__gt=0)
    emails = []
    for book in books:
        follows = Follow.objects.filter(book_id=book.id)
        for follow in follows:
            emails.append(follow.user.email)
        send_mail(
            subject="BiblioteKa Info, Disponibilidade do Livro!",
            message=f"Uhuuu! o livro {book.title} que você segue, já está disponível...",
            from_email=os.getenv("EMAIL_HOST_USER"),
            recipient_list=emails,
            fail_silently=False,
        )


class BookSchedulerJob(Job):
    @staticmethod
    def run():
        send_emails()
