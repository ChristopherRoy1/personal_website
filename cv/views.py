from django.shortcuts import render, HttpResponse
from cv.models import WorkItem
# Create your views here.
def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Chris Roy'

    work_experience = WorkItem.objects.all()
    print(work_experience)
    args = {'name': name, 'numbers': numbers, 'work_experience_items': work_experience}

    return render(request, 'cv/home.html', args)
