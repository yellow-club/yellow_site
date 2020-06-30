from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, Category
from events.models import Event
from django.db.models import F

class Home(ListView):
    model = Event
    template_name = 'yellow_site/index.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Официальный сайт 1С сообщества Желтый Клуб'
        return context
    
    def get_queryset(self):
        return Event.objects.filter(is_published = True)

class GetPost(DetailView):
    model = Post
    template_name = 'yellow_site/post.html'  
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

class GetAllPost(ListView):
    model = Post
    template_name = 'yellow_site/all_posts.html'  
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статьи'
        return context
