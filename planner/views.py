from django.shortcuts import render,get_object_or_404,redirect
from .models import Planner
from django.utils import timezone
from .forms import PlannerForm
# Create your views here.

def home(request):
    planner_list=Planner.objects.all().order_by('created_date')
    return render(request,'planner/home.html',{'planners':planner_list})

def detail(request, planner_id):
    planner_detail=get_object_or_404(Planner,pk=planner_id)
    return render(request,'planner/detail.html',{'planner':planner_detail})

def planner_new(request):
    if request.method=="POST":
        form=PlannerForm(request.POST)
        if form.is_valid():
            planner=form.save(commit=False)
            planner.published_date=timezone.datetime.now()
            planner.save()
            return redirect('detail',planner_id=planner.pk)
    else:
        form=PlannerForm()
    return render(request,'planner/planner_new.html',{'form':form})

def planner_edit(request,planner_id):
    planner=get_object_or_404(Planner,pk=planner_id)
    if request.method=="POST":
        form=PlannerForm(request.POST,instance=planner)
        if form.is_valid():
            planner=form.save(commit=False)
            planner.published_date=timezone.datetime.now()
            planner.save()
            return redirect('detail',planner_id=planner.pk)
    else:
        form=PlannerForm(instance=planner)
    return render(request,'planner/planner_edit.html',{'form':form})

def planner_delete(request,planner_id):
    planner=get_object_or_404(Planner,pk=planner_id)
    planner.delete()
    return redirect('home')