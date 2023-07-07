from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

from .models import Loans
from .serializers import LoansSerializer
from users.permissions import IsLibraryCollaboratorOrOwner
from users.models import User
from rest_framework.exceptions import PermissionDenied, ValidationError


class LoanView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    queryset = Loans.objects.filter(is_returned=False)
    serializer_class = LoansSerializer

    def perform_create(self, serializer):
        data_atual = datetime.now()
        user = self.request.user
        is_delay = Loans.objects.filter(user=user, is_delay=True)

        if is_delay:
            raise ValidationError({"detail": "User is blocked for delay"})

        blocking_dates = Loans.objects.filter(
            user=user, blocking_date__lt=make_aware(data_atual)
        )

        if blocking_dates.exists():
            raise ValidationError({"detail": "User is blocked"})

        registros_atrasados = Loans.objects.filter(
            loan_return__lt=make_aware(data_atual)
        )

        if registros_atrasados.exists():
            raise ValidationError({"detail": "User with delay in returning loans"})

        user = self.request.user

        if not user.is_allowed:
            raise PermissionDenied({"detail": "You are not allowed to borrow books."})

        serializer.save(user=user)


class LoanDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    queryset = Loans.objects.all()
    serializer_class = LoansSerializer
    lookup_url_kwarg = "pk"
