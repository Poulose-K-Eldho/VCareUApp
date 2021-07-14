from django.db import models
from django.urls import reverse
# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    desc=models.TextField()
    img=models.ImageField(upload_to="department")
    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural = 'departments'
    def get_url(self):
        return reverse("VCareUApp:doctors_department",args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)


class Doctor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    age = models.IntegerField()
    img = models.ImageField(upload_to="doctor")
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    gender=models.TextField(choices=(("male","male"),("female","female")))
    available=models.BooleanField(default=True)
    email=models.EmailField(blank=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'
    def get_url(self):
        return reverse('VCareUApp:DocDetail',args=[self.department.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)
