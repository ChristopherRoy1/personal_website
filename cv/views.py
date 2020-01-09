from django.shortcuts import render, HttpResponse
from cv.models import WorkItem, WorkItemBullet
# Create your views here.
def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Chris Roy'

    work_experience_bullets = WorkItemBullet.objects.all()
    work_items = WorkItem.objects.all()


    args = {'name': name, 'numbers': numbers, \
            'work_experience_items': work_items}

    return render(request, 'cv/home.html', args)
