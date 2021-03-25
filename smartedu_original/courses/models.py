from django.db import models
from teachers.models import Teacher

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=250,unique=True, verbose_name="Course name", help_text="Enter course name, please")
    teacher = models.ForeignKey(Teacher, null=True , on_delete=models.CASCADE)
    category = models.ForeignKey(Category,null=True, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, blank=True, null=True,)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="courses/%d/%m/%y", default = "courses/default_course_image.jpg")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
