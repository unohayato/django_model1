from django.views.generic import ListView, DetailView

from .models import Post
# Create your views here.

class Index(ListView):
  model = Post

class Detail(DetailView):
  model = Post
