from django.shortcuts import render
import datetime

# Create your views here.
def newyears(request):
    now = datetime.datetime.now()
    context = {
        'response' : now.month == 1 and now.day == 1
    }
    return render(request, 'newyears.html', context)