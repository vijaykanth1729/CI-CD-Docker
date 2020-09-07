from django.db import models
#from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.TextField()
    income = models.DecimalField(max_digits=10, decimal_places=2)
    #photo = models.ImageField(upload_to='photos/'%Y/%m/%d')
    def __str__(self):
        return f"{self.name}"

    # def get_absolute_url(self):
    #     return reverse("student_app:detail", kwargs={'pk':self.pk})
