from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PostForm
from webapp.models import Post


class PostsListView(ListView):
    model = Post
    template_name = "posts/posts_list.html"
    context_object_name = "posts"
    paginate_by = 3
    ordering = ("-created_at",)

    def get_queryset(self):
        return super().get_queryset()


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = "posts/post_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_update.html"

    def has_permission(self):
        return self.request.user == self.get_object().author


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete.html"

    def has_permission(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.request.user.pk})


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = "posts/post_view.html"
