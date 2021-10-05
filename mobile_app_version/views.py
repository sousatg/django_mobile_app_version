from django.http import JsonResponse, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist

from .models import MobileAppVersion

def get_by_manufactor(request, manufactor):
    try:
        mobile_app_version = MobileAppVersion.objects.get(manufactor=manufactor)
    except ObjectDoesNotExist:
        return HttpResponseBadRequest()

    return JsonResponse(mobile_app_version.serialize())

def get_all(request):
    mobile_app_versions = MobileAppVersion.objects.all()
    mobile_app_versions = [el.serialize() for el in mobile_app_versions]

    return JsonResponse(mobile_app_versions, safe=False)
