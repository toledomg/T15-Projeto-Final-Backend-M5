from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime, timedelta, timezone

from users.serializers import UserSerializer
from .models import Loans
from users.models import User
from .serializers import LoansSerializer
from users.permissions import IsLibraryCollaboratorOrOwner
from rest_framework.exceptions import PermissionDenied, ValidationError
from django.utils.timezone import make_aware, get_default_timezone


class LoanView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    queryset = Loans.objects.filter(is_returned=False)
    serializer_class = LoansSerializer
    lookup_url_kwarg = "pk"

    def perform_create(self, serializer):
        data_atual = datetime.now()
        user_id = self.request.data.get("user_id")
        user = User.objects.get(id=user_id)

        is_delay = Loans.objects.filter(user=user, is_delay=True)

        if is_delay:
            raise ValidationError({"detail": f"User is blocked for delay "})

        blocking_dates = Loans.objects.filter(
            user=user, blocking_date__lt=make_aware(data_atual)
        )

        if blocking_dates.exists():
            raise ValidationError({"detail": "User is blocked"})

        registros_atrasados = Loans.objects.filter(
            loan_return__lt=make_aware(data_atual)
        )

        if registros_atrasados.exists():
            data_now = datetime.now()
            for registro in registros_atrasados:
                delay = data_now.date() - registro.loan_return.date()
                delay_days = delay.days
                raise ValidationError(
                    {"detail": f"User count overdue records by {delay_days} days"}
                )

        if not user.is_allowed:
            raise PermissionDenied({"detail": "You are not allowed to borrow books."})

        serializer.save(user=user)
        # instance.loan_return = None
        # instance.copy.is_available = True
        # instance.copy.save()

        # instance.is_returned = True
        # instance.save()


class LoanDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    queryset = Loans.objects.all()
    serializer_class = LoansSerializer
    lookup_url_kwarg = "pk"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.is_returned:
            return Response(
                {"details": "This book has already been returned."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        current_datetime = datetime.now()
        return_deadline = instance.loan_return.date()

        if current_datetime.date() > return_deadline:
            instance.blocking_date = current_datetime + timedelta(days=7)
            instance.save()

            # instance.user.is_allowed = False
            # instance.user.save()

            instance.loan_return = None
            instance.copy.is_available = True
            instance.copy.save()

            instance.is_returned = True
            instance.save()            

            return Response(
                {
                    "info": "This book has already been returned",
                    "details": f"Return deadline has been exceeded, user is blocked until {instance.blocking_date}.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        instance.loan_return = None
        instance.copy.is_available = True
        instance.copy.save()

        instance.is_returned = True
        instance.save()

        serializer = self.get_serializer(instance)

        return Response(serializer.data)


class UserLoansDetailView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    serializer_class = LoansSerializer

    def get_queryset(self):
        instance_user = self.request.user
        queryset = Loans.objects.filter(user=instance_user)

        return queryset
