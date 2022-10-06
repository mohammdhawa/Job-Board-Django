from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

'''
Django model field:
    -html widget
    -validation
    -db size
'''

class Job(models.Model):
    JOBTYPE = (
        ('full time', 'full time'),
        ('part time', 'part time'),
    )
    
    def image_upload(instance, filename):
        imagename , extension = filename.split(".")
        return "jobs/%s.%s"%(instance.id, extension)
    
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100) # column
    # location = 
    job_type = models.CharField(max_length=20, choices=JOBTYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Logic
        self.slug = slugify(self.title) 
        super(Job,self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.title)



class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.name)


class Apply(models.Model):
    
    def cv_upload(instance, filename):
        fname, extension = filename.split(".")
        name = instance.name.replace(' ', '_')
        return "apply/%s.%s"%(name, extension)
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.URLField()
    cv = models.FileField(upload_to=cv_upload)
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)