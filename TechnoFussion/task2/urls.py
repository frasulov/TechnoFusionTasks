from django.urls import path
from .views import *
from .viewsets import urlpatterns as rest_urls
urlpatterns = [
    path("generate-labels/<str:suppCode>", LabelView.as_view(), name = "label_view")
]

urlpatterns += rest_urls