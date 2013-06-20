# Create your views here.
from django.template.response import TemplateResponse
from flickr.models import Photo


def index(request):
    photos = Photo.objects.filter(
        flickr_id__in=['5707927156', '5714106535', '5745247320', ]

    )
    return TemplateResponse(request, 'index.html', context={
        'photos': photos,
    })
