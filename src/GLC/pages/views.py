from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from about.models import About, header, category, numbers
from home.models import Topbar, Head, Footer
from graduates.models import Graduate
from team.models import Team
from gallerys.models import Photo
from events.models import Event
from accounts.models import Profile
from announcements.models import Announcement
from contact.models import Contact
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import (
    ListView,
)

# Dont Repeat Yourself = DRY

def index(request):
    abouts = About.objects.order_by('-reload').filter(is_published=True)[:1]
    graduates = Graduate.objects.order_by('-timestamp').filter(is_published=True)[:1]
    numberss = numbers.objects.order_by('reload').filter(is_published=True)[:4]
    teams = Team.objects.order_by('-timestamp').filter(is_published=True)[:4]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    heads = Head.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    categorys = category.objects.order_by('-reload').filter(is_published=True)[:4]
    photos = Photo.objects.order_by('-reload').filter(is_published=True)[:8]
    accounts = Profile.objects.all()

    context = {
        'events': Event.objects.all()[:3],
        'abouts': abouts,
        'graduates': graduates,
        'numberss': numberss,
        'accounts': accounts,
        'topbars': topbars,
        'heads': heads,
        'footers': footers,
        'teams': teams,
        'categorys': categorys,
        'photos': photos,
    }
    return render(request, 'pages/index.html', context) 


class EventListView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'
    ordering = ['-created_on']
    paginate_by = 5

def about(request):
    teams = Team.objects.order_by('-timestamp').filter(is_published=True)[:4]
    abouts = About.objects.order_by('-reload').filter(is_published=True)[:1]
    headers = header.objects.order_by('-reload').filter(is_published=True)[:1]
    categorys = category.objects.order_by('reload').filter(is_published=True)
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
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

@staff_member_required
def dashboard(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    announcements = Announcement.objects.order_by('-timestamp').filter(is_published=True)[:10]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    contacts = Contact.objects.order_by('-timestamp').filter(is_published=True)[:4]
    num_teams = Team.objects.count()
    num_contacts = Contact.objects.count()
    num_announcements = Announcement.objects.count()
    num_events = Event.objects.count()
    num_photos = Photo.objects.count()
    num_profiles = Profile.objects.count()

    context = {
        'contacts': contacts, 
        'num_profiles' : num_profiles,
        'num_teams': num_teams,
        'num_photos': num_photos,
        'num_contacts': num_contacts,
        'num_events': num_events,
        'announcements': announcements,
        'topbars': topbars,
        'footers': footers,
        
    }
    return render(request, 'pages/dashboard.html', context=context) 

    def message(request):
         contact = get_object_or_404(Event, pk=event_id)
         context = {
             'contact':contact

         }
         return render(request, 'pages/contact.html', context)
 
    
  