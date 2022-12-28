from rest_framework.generics import(ListAPIView, CreateAPIView, )
from django.views.generic.base import RedirectView
from APP.models import MASSAGE
from .serializers import CraetSerislizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class MassageCreatAPIView(CreateAPIView):
    queryset = MASSAGE.objects.all()
    serializer_class = CraetSerislizer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





