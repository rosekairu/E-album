from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Category,Location
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
  """
  View function that renders the index page
  """
  photos = Image.get_all_images()
  return render(request,'album/index.html',{"photos":photos})


def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"album/index.html", {"image":image})


def search_image(request):
  
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_image(category)
        message = f"{category}"

        return render(request, 'album/search.html',{"message":message,"images": searched_images})
    else:
        message = ".You haven't searched for any category"
        return render(request, 'album/search.html',{"message":message})


def filter_by_location(request,location_id):
    '''
    Filters the database and displays images according to location_id
    '''
    images = Image.filter_by_location(id=location_id)
    return render(request, 'album/location.html', {"images": images})


def filter_by_category(request,category_id):
    '''
    Filters the database and displays images according to category_id
    '''
    images = Image.filter_by_category(id = category_id)
    return render(request,'album/category.html',{"images":images})
