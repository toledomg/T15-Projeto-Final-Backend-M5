from rest_framework import generics
from .models import Loans
from .serializers import LoansSerializer


class LoanView(generics.ListCreateAPIView):
    queryset = Loans.objects.filter(is_returned=False)
    serializer_class = LoansSerializer


class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer

    def perform_destroy(self, instance):
        if instance.is_returned:
            instance.copy.quantity += 1
            instance.copy.save()

            instance.copy.is_returned = True
            instance.copy.save()

            instance.is_returned = True
            instance.save()
