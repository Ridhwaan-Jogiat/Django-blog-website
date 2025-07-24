from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import CreateView, UpdateView, DeleteView,ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin



# Create your views here.

""" def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {"posts": posts})
 """
# View details of a post

@login_required
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})

#crud operations
# New post


class PostCreateView(CreateView,LoginRequiredMixin):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user  # auto-fill author
        return super().form_valid(form)

# Update a post


class PostUpdateView(UpdateView,UserPassesTestMixin,LoginRequiredMixin):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Delete a post
class PostDeleteView(DeleteView,UserPassesTestMixin,LoginRequiredMixin):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostListView(ListView):
    model=Post
    template_name="blog/home.html"
    context_object_name = "posts"
    ordering = ['-created_at']
