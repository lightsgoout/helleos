# Create your views here.
from django.conf import settings
from django.http import Http404
from django.template.response import TemplateResponse
from flickr.models import Photo, PhotoSet


def index(request):
    return by_category(request, settings.FULLSCREEN_PHOTOSET, fullscreen=True)


def by_category(request, category, fullscreen=False):
    category = category.replace('_', ' ').replace('-', ' ')
    try:
        flickr_category = PhotoSet.objects.get(
            title=category
        )
    except PhotoSet.DoesNotExist:
        raise Http404

    photos = flickr_category.photos.all()[0:5]
    return TemplateResponse(request, 'index.html', context={
        'photos': photos,
        'fullscreen': fullscreen,
    })


