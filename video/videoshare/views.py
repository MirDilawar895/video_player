from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Video
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


class Index(ListView):
    model = Video
    template_name = 'index.html'
    order_by = 'date_posted'


class CreateVideo(CreateView):
    model = Video
    fields = ['title', 'description', 'video_file', 'thumbnail']
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})


class DetailVideo(DetailView):
    model = Video
    template_name = 'detail_video.html'


class UpdateVideo(UpdateView):
    model = Video
    fields = ['title', 'description']
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})


class DeleteVideo(DeleteView):
    model = Video
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('index')
