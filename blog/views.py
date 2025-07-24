from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {"posts": posts})

# View details of a post

@login_required
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})

#crud operations
# New post


class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("home")

# Update a post


class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("home")


# Delete a post
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("home")
