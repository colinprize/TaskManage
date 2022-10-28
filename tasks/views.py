from django.shortcuts import render, redirect, get_object_or_404
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.assignee = request.user
            task.save()
            return redirect("home")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)

@login_required
def show_my_tasks(request):
    task = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": task
    }
    return render(request, "tasks/list.html", context)
