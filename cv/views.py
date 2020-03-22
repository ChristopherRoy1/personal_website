from django.shortcuts import render, HttpResponse
from cv.models import WorkItem, WorkItemBullet, EducationItem
# Create your views here.
def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Chris Roy'

    work_experience_bullets = WorkItemBullet.objects.all()
    work_items = WorkItem.objects.all()

    education_items = EducationItem.objects.all()

    args = {'name': name, 'numbers': numbers, \
            'work_experience_items': work_items, \
            'education_items': education_items}

    return render(request, 'cv/index.html', args)
