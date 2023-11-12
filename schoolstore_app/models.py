from django.db import models
from django.urls import reverse


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def get_url(self):
        return reverse('schoolstore_app:courses_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Course(models.Model):
    name = models.CharField(max_length=250)
    year = models.IntegerField()
    duration = models.TextField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def get_url(self):
        return reverse('schoolstore_app:crsdptdetail', args=[self.department.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)
