from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime
from .models import Loans
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
            raise ValidationError(
                {"detail": "User with delay in returning loans"})

        user = self.request.user

        if not user.is_allowed:
            raise PermissionDenied(
                {"detail": "You are not allowed to borrow books."})

        serializer.save(user=user)


class LoanDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    queryset = Loans.objects.all()
    serializer_class = LoansSerializer
    lookup_url_kwarg = "pk"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.is_returned:
            return Response({"error": "Este livro já foi devolvido."},
                            status=status.HTTP_400_BAD_REQUEST)

        current_datetime = datetime.now()
        return_deadline = instance.loan_return.date()

        if current_datetime.date() > return_deadline:
            return Response(
                {"error": "A data limite de devolução foi ultrapassada."},
                status=status.HTTP_400_BAD_REQUEST)

        instance.loan_return = make_aware(current_datetime)
        instance.copy.is_available = True
        instance.copy.save()
        instance.is_returned = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
