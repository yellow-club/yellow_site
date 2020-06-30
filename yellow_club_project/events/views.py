from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Event, Category
from django.db.models import F

class GetEvent(DetailView):
    model = Event
    template_name = 'events/event.html'  
    context_object_name = 'event'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

class GetAllEvents(ListView):
    model = Event
    template_name = 'events/all_events.html'  
    context_object_name = 'events'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мероприятия с Желтым Клубом'
        return context

    def get_queryset(self):
        return Event.objects.filter(is_published = True)


