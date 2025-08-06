from urllib.parse import urlencode

from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DetailView, ListView

from accounts.forms import MyUserCreationForm
from webapp.forms import SearchForm


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:index')
        return next_url


class ProfileView(DetailView):
    model = get_user_model()
    template_name = "profile.html"
    context_object_name = "user_obj"


class FollowersView(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(get_user_model(), pk=pk)
        if user == request.user:
            return HttpResponseBadRequest("На себя не подписываются")
        if request.user in user.followers.all():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
        return redirect('accounts:profile', pk=pk)


class UserListView(ListView):
    template_name = 'users.html'
    model = get_user_model()
    context_object_name = "users"

    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(username__icontains=self.search_value) | Q(email__icontains=self.search_value))
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
