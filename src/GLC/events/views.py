from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from home.models import Footer, Topbar
from django.contrib.auth.models import User 
from .models import Event


def events(request):
    events = Event.objects.order_by('-timestamp').filter(is_published=True)
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]

    paginator = Paginator(events, 3)
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)

    context = {
        'events': paged_events,
        'topbars': topbars,
        'footers': footers

    }
    return render(request, 'events/events.html', context)

def event(request, event_id):
    events = Event.objects.order_by('timestamp').filter(is_published=True)[:10]
    event = get_object_or_404(Event, pk=event_id)
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]

    context = {
        'events': events,
        'event': event,
        'topbars': topbars,
        'footers': footers
    
    }
    return render(request, 'events/event.html', context)


