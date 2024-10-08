from django.db import models
from django.utils.text import slugify
# Create your models here.
def upload_job(instance,file_name):
    extention=file_name.split('.')[1]
    return f'job/{instance.job_name}.{extention}'

job_type=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)

class Job(models.Model):
    job_name=models.CharField(max_length=200)
    slug=models.SlugField(unique=True,blank=True,null=True)
    image=models.ImageField(upload_to=upload_job,width_field=None,height_field=None)
    place=models.CharField(max_length=200)
    type_job=models.CharField(max_length=200,choices=job_type)
    salary=models.IntegerField(default=0)
    vacancy=models.IntegerField(default=0)
    description=models.TextField(max_length=900)
    qualifications=models.TextField(max_length=900)
    date=models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.job_name)
        super(Job,self).save(*args,**kwargs)


    class Meta:
        verbose_name=("Job")
        verbose_name_plural=("Jobs")
    
    def __str__(self):
        return self.job_name
    
def upload_cv(instance,file_name):
    extention=file_name.split('.')[1]
    return f'CV/{instance.name}.{extention}'
    
class Apply(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    mail=models.EmailField(max_length=300)
    web=models.CharField(max_length=700)
    cv=models.FileField(upload_to=upload_cv)
    cover=models.TextField(max_length=700,null=True,blank=True)

    class Meta:
        verbose_name=("Apply")
        verbose_name_plural=("Applies")
    
    def __str__(self):
        return self.name
