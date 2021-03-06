from django.db import models


class Host(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True)
    bio = models.TextField(default='')

    class Meta:
        verbose_name = 'Host'
        verbose_name_plural = 'Hosts'

    def __str__(self):
        return self.name


class Overview(models.Model):
    week = models.CharField(max_length=20)
    monday = models.TextField(default='')
    tuesday = models.TextField(default='')
    wednesday = models.TextField(default='')
    thursday = models.TextField(default='')
    friday = models.TextField(default='')

    def __str__(self):
        return self.week


class Project(models.Model):
    authors = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    repo = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Projects'


    def __str__(self):
        return self.name


class FeedBack(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    notes = models.TextField(default='')

    class Meta:
        verbose_name_plural = 'FeedBacks'


    def __str__(self):
        return self.name
