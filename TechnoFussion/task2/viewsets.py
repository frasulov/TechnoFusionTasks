from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from .serializers import *
from .models import *

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class SuppSeqViewSet(viewsets.ModelViewSet):
    queryset = SuppSeq.objects.all()
    serializer_class = SuppSeqSerializer


class LabelsViewSet(viewsets.ModelViewSet):
    queryset = Labels.objects.all()
    serializer_class = LabelsSerializer


router = DefaultRouter()
router.register('requests', RequestViewSet)
router.register('labels', LabelsViewSet)
router.register('suppseqs', SuppSeqViewSet)

urlpatterns = router.urls