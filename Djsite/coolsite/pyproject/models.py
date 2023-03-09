from django.db import models
from django.urls import reverse

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")
    category = models.ForeignKey('Category', on_delete=models.PROTECT)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def str(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})


class Training_manager1(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    speciality = models.TextField()
    number = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")


class Training_manager2(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    speciality = models.TextField()
    number = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")


class Motivation(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.TextField(blank=True)



class Training2(models.Model):
    title = models.CharField(max_length=255)
    time = models.TextField()
    place = models.TextField()
    training_manager = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")

class Training1(models.Model):
    title = models.CharField(max_length=255)
    time = models.TextField()
    place = models.TextField()
    training_manager = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")


