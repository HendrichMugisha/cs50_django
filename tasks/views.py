from django.shortcuts import render

# Create your views here.
def index(request):
    tasks = ['nice', 'not nice', 'nothing']
    context = {
        'tasks' : tasks
    }
    return render(request, 'tasks.html', context)

def add_task(request):
    return render(request, 'add_task.html')