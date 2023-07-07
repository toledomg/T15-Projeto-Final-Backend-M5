from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime
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
        user = self.request.user

        if not user.is_allowed:
            raise PermissionDenied("You are not allowed to borrow books.")

        data_atual = datetime.now()
        registros_atrasados = Loans.objects.filter(loan_return__lt=make_aware(data_atual))
        print(registros_atrasados)

        # Verifica se existem registros em atraso
        if registros_atrasados.exists():
            # Gera uma mensagem de erro
            raise ValidationError({"detail": "Usuário com atraso na devolução dos empréstimos:"})
        
        serializer.save(user=user)


class LoanDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    queryset = Loans.objects.all()
    serializer_class = LoansSerializer
    lookup_url_kwarg = "pk"


    # def perform_destroy(self, instance):
    #     if instance.is_returned:
    #         instance.copy.quantity += 1
    #         instance.copy.save()

    #         instance.copy.is_returned = True
    #         instance.copy.save()

    #         instance.is_returned = True
    #         instance.save()

