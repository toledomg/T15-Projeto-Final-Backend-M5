from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Loans
from .serializers import LoansSerializer
from users.permissions import IsLibraryCollaboratorOrOwner


class LoanView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    queryset = Loans.objects.filter(is_returned=False)
    serializer_class = LoansSerializer


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
