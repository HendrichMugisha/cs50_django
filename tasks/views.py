from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

tasks = []
# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    context = {
        'tasks' : request.session["tasks"]
    }
    return render(request, 'tasks.html', context)

def add_task(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session["tasks"] += [task]
            # print(task)
            return HttpResponseRedirect(reverse("tasks:home"))
        else:
            return render(request, 'add_task.html', {
                "form" : form
            })

    return render(request, 'add_task.html', {"form": NewTaskForm()})
        