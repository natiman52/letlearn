from django.db import models
from ckeditor.fields import RichTextField
import datetime
from django.template.defaultfilters import slugify
# Create your models here.
class Vedios(models.Model):
    identifier =models.CharField(max_length=250,default="Blank")
    video = models.URLField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.identifier
class Chapter(models.Model):
    title = models.CharField(max_length=45)
    desc = RichTextField(blank=True,null=True)
    video = models.URLField(max_length=500,null=True,blank=True)
    additional_video = models.ManyToManyField(Vedios,blank=True,null=True)
    conclusion = RichTextField(blank=True,null=True)
    identifier = models.CharField(max_length=200,null=True)
    slug =models.CharField(unique=True,null=True,blank=True,max_length=250)
    def __str__(self) -> str:
        return self.identifier
    def save(self,*args,**kwargs):
        slug = slugify(self.title)
        self.slug =f"{self.identifier}-{slug}"
        super(Chapter, self).save(*args, **kwargs)

class Unit(models.Model):
    title =models.CharField(max_length=45)
    chapters =models.ManyToManyField(to=Chapter ,blank=True,through='UnitAndChapter')
    identifier = models.CharField(max_length=200,null=True)
    def __str__(self) -> str:
        return self.identifier
class tutorial(models.Model):
    name =models.CharField(max_length=45)
    desc = models.TextField()
    image=models.ImageField(upload_to='images')
    date =models.DateField(default=datetime.date.today)
    units = models.ManyToManyField(to=Unit,blank=True,through="UnitAndTutorial")
    def __str__(self) -> str:
        return self.name
class collection(models.Model):
    name =models.CharField(max_length=45)
    image=models.ImageField(upload_to='images')
    desc = models.TextField()
    date =models.DateField(default=datetime.date.today)
    courses = models.ManyToManyField(to=tutorial)    
    def __str__(self):
        return self.name
class UnitAndTutorial(models.Model):
    Tutorial = models.ForeignKey(to=tutorial,on_delete=models.CASCADE)
    unit = models.ForeignKey(to=Unit,on_delete=models.CASCADE)
    index = models.IntegerField()

class UnitAndChapter(models.Model):
    Chapter = models.ForeignKey(to=Chapter,on_delete=models.CASCADE)
    unit = models.ForeignKey(to=Unit,on_delete=models.CASCADE)
    index = models.IntegerField()    

class Request(models.Model):
    name = models.CharField(max_length=250)
    courseName = models.CharField(max_length=250)
    desc =models.TextField()
    date =models.DateField(default=datetime.date.today)