from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

from loans.utils import ResponseMethods

from .models import Loans
from .serializers import LoansSerializer
from users.permissions import IsLibraryCollaboratorOrOwner
from users.models import User
from rest_framework.exceptions import PermissionDenied, ValidationError
from django.utils import timezone
from copies.models import Copy


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
        # if not instance.loan_return is not None:
        #     return Response({"error": "Este livro já foi devolvido."}, status=status.HTTP_400_BAD_REQUEST)
        instance.loan_return = make_aware(datetime.now())
        instance.copy.is_available = True
        instance.copy.save()
        instance.is_returned = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # def patch(self, request, *args, **kwargs):
    #     loans = self.get_object()

    #     if loans.is_returned:
    #         return ResponseMethods.response_error(
    #             400, {"detail": "O livro já foi devolvido."})

    #     loan_return = loans.loan_return
    #     if loan_return < timezone.now():
    #         loans.blocking_date = timezone.now() + timedelta(days=7)

    #     loans.is_returned = True
    #     loans.save()
    #     copy = loans.copy
    #     copy.is_available = True
    #     copy.save()

    #     return ResponseMethods.response_success(
    #         200, {"detail": "Livro devolvido com sucesso."})

    # def return_book(self, loan_id):
    #     try:
    #         loan = Loans.objects.get(id=loan_id)
    #     except Loans.DoesNotExist:
    #         raise ValidationError({"details": "Empréstimo não encontrado"})
    #     if loan.is_returned:
    #         raise ValidationError({"details": "Este livro já foi devolvido"})
    #     loan.is_returned = True
    #     loan.save()
    #     copy = loan.copy
    #     copy.is_available = True
    #     copy.save()
    #     return loan
