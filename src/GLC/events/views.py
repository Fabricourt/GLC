from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from home.models import Footer, Topbar, Head
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Event




def event(request):
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    context = {
        'topbars': topbars,
        'footers': footers,
        'events': Event.objects.all(),
       
    }
    return render(request, 'events/events.html', context)


class EventListView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'
    ordering = ['-created_on']
    paginate_by = 5


class UserEventListView(ListView):
    model = Event
    template_name = 'events/user_events.html'
    context_object_name = 'events'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Event.objects.filter(event_name=user).order_by('-created_on')


class EventDetailView(DetailView):
    model = Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = []
    
    def form_valid(self, form):
        form.instance.event_name = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = []

    def form_valid(self, form):
        form.instance.event_name = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.event_name:
            return True
        return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == event.author:
            return True
        return False
