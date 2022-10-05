from django.shortcuts import render, redirect
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyJob

# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'jobs': page_obj}
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
