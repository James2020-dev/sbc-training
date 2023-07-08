from django.db import models
from django.urls import reverse

class Courses(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('our-courses')

class sub_Courses(models.Model):
    name = models.CharField(max_length=255)
    course=models.ForeignKey(Courses, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_sub_course_all')