from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import (
    ListView,
    CreateView,
)
# Create your views here.

class PostListView(ListView):
    template_name='clone/post_list'
    queryset = Post.objects.all()
    context_object_name = "posts"
    
class PostCreateView(CreateView):
    template='clone/post_create.html'
    form_class = PostForm
    queryset = Post.objects.all()
    
    def form_valid(self,form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)

