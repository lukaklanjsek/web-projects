from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView

from .models import Task



# Create your views here.

class CustomLoginView(LoginView):
    template_name = "base_app/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


class CustomLogoutView(LogoutView):
    template_name = "base_app/logout1.html"
    fields = "__all__"



class TaskList(ListView):
    model = Task
    context_object_name = "tasks"


class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "base_app/task.html"


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class DeleteView(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")