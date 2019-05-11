from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from about.models import About, header, category
from home.models import Topbar, Head, Footer
from team.models import Team
from gallery.models import gallery
from users.models import Profile
from django.contrib.admin.views.decorators import staff_member_required

# Dont Repeat Yourself = DRY

def index(request):
    teams = Team.objects.order_by('-timestamp').filter(is_published=True)[:4]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    heads = Head.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    categorys = category.objects.order_by('-reload').filter(is_published=True)[:4]
    gallerys = gallery.objects.order_by('-reload').filter(is_published=True)[:6]
    users = Profile.objects.all()

    context = {
        'topbars': topbars,
        'heads': heads,
        'footers': footers,
        'teams': teams,
        'categorys': categorys,
        'gallerys': gallerys,
    }
    return render(request, 'pages/index.html', context) 


def about(request):
    teams = Team.objects.order_by('-timestamp').filter(is_published=True)[:4]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    abouts = About.objects.order_by('-reload').filter(is_published=True)[:1]
    headers = header.objects.order_by('-reload').filter(is_published=True)[:1]
    categorys = category.objects.order_by('reload').filter(is_published=True)
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    
    context = {
        'topbars': topbars,
        'teams': teams,
        'headers': headers,
        'categorys': categorys,
        'abouts': abouts,
        'footers': footers
    }
    return render(request, 'pages/about.html', context) 

@staff_member_required
def mobile(request):
    return render(request, 'pages/mobile.html') 

@staff_member_required
def tablet(request):
    return render(request, 'pages/tablet.html') 

@staff_member_required
def laptop(request):
    return render(request, 'pages/laptop.html') 