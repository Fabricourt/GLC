from django.shortcuts import render
from home.models import Footer, Topbar

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from home.models import Topbar, Head
from.models import gallery

def index(request):
  gallerys = gallery.objects.order_by('-reload').filter(is_published=True)
  topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
  footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
  paginator = Paginator(gallerys, 12)
  page = request.GET.get('page')
  paged_gallerys = paginator.get_page(page)

  context = {
    'gallerys': paged_gallerys,
    'topbars': topbars,
    'footers': footers
  }

  return render(request, 'gallery/gallerys.html', context)



def gallery_detail(request, gallery_id):
  gallery = get_object_or_404(gallery, pk=gallery_id)
  topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
  footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
 
  context = {
    'gallery': gallery,
    'topbars': topbars,
    'footers': footers
    
  }

  return render(request, 'gallery/gallery.html', context)
