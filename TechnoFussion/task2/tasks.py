from celery import shared_task
from .models import Labels

@shared_task()
def createNewLabel(label_no, requestId):
    try:
        labels = Labels()
        labels.labelNo = label_no
        labels.requestId = requestId
        labels.save()
        return 1
    except:
        return 0
