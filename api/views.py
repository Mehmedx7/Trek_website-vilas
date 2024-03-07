from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    header_object = Header.objects.all()
    popular_destination_object = Popular_destination.objects.all()
    packages_objects = Packages.objects.all()
    Photo_gallery_objects = Photo_gallery.objects.all()
    call_to_action_object = Call_to_action.objects.all()
    footer_objects = footer.objects.all()

    context = {
        'header_object': header_object,
        'popular_destination_object': popular_destination_object,
        'packages_objects': packages_objects,
        'Photo_gallery_objects': Photo_gallery_objects,
        'call_to_action_object': call_to_action_object,
        'footer_objects': footer_objects
    }

    return render(request, 'index.html', context)