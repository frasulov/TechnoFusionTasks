from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import *
from django.http import JsonResponse
from datetime import datetime
from .util import getXDigitInteger
from .tasks import createNewLabel
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class LabelView(View):

    def post(self, request, suppCode):
        request_instance = None
        try:
            request_instance = Request.objects.get(suppCode=suppCode, status=Request.Status.OPEN)
        except ObjectDoesNotExist:
            return JsonResponse({"message": "No such Request"})

        year = str(datetime.now().year)
        year = year[len(year)-2:] # get last digits of current year
        try:
            suppSeq = SuppSeq.objects.get(suppCode=suppCode, year=year)
            print(suppCode, "year", year)
            print(suppSeq)
            for i in range(1, request_instance.fullBarchQty+1):

                for j in range(1, request_instance.fullLabelsQty+1):
                    label = f"{year}-{suppCode}-{getXDigitInteger(suppSeq.seq)}-{getXDigitInteger(j,5)}"
                    createNewLabel.delay(label, request_instance.id)
                suppSeq.seq = suppSeq.seq + 1 # increse seq

            for i in range(1, request_instance.lastBatchQty+1):

                for j in range(1, request_instance.lastLabelQty+1):
                    label = f"{year}-{suppCode}-{getXDigitInteger(suppSeq.seq)}-{getXDigitInteger(j,5)}"
                    createNewLabel.delay(label, request_instance.id)
                suppSeq.seq = suppSeq.seq + 1

            suppSeq.save()
            request_instance.status = Request.Status.GENERATED
            request_instance.save() # update request status to Generated
            return JsonResponse({"message":"Labels created!"})
        except ObjectDoesNotExist:
            return JsonResponse({"message": "No such SuppSeq"})
