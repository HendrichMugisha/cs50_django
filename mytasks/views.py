from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
class MyTaskssForm(forms.Form):
    task = forms.CharField(max_length=100, label="Newtask")
    is_completed = forms.BooleanField(label='tick if completed')
    priority = forms.IntegerField(max_value= 10, min_value=1, label="Task priority")


tasks = ['none', 'none at all', 'absolutely nothing']
def mytasks(request):
    context = {
        'tasks' : tasks
    }
    return render(request, 'mytasks.html', context)

def addtask(request):
    if request.method == 'POST':
        form = MyTaskssForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            tasks.append(task)
            return redirect('mytasks:home')
        else:
            return render(request, 'addmytask.html', {"form" : form})
    
    return render(request, 'addmytask.html', { "form" : MyTaskssForm()})