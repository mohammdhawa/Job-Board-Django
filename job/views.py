from django.shortcuts import render, redirect
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyJob, AddJob
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    jobs_count = jobs.count()
    
    # Filters 
    myfilter = JobFilter(request.GET, queryset=jobs)
    jobs = myfilter.qs
    
    paginator = Paginator(jobs, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'jobs': page_obj, 'myfilter': myfilter, 'jobs_count': jobs_count}
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job = Job.objects.get(slug=slug)
    
    if request.method == "POST":
        form = ApplyJob(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()
    else:
        form = ApplyJob()
    
    context = {'job': job, 'form': form}
    return render(request, 'job/job_detail.html', context)


@login_required
def add_job(request):
    
    if request.method == 'POST':
        myform = AddJob(request.POST, request.FILES)
        if myform.is_valid():
            form = myform.save(commit=False)
            form.owner = request.user
            form.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = AddJob()
    
    context = {'form': form}
    return render(request, 'job/add_job.html', context)
