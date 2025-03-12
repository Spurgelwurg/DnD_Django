# from django.db import models

# class Campaign(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     start_date = models.DateField()

#     def __str__(self):
#         return self.name
    
# class NPC(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Enemy(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
    
# class Location(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Event(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     date = models.DateField()
#     campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Task(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     is_completed = models.BooleanField(default=False)
#     Campaign = models.ForeignKey(Campaign, related_name='task', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
    
# class Note(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     campaign = models.ForeignKey(Campaign, related_name='notes', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

# class File(models.Model):
#     file = models.FileField(upload_to='campaign_files/')
#     description = models.TextField()
#     campaign = models.ForeignKey(Campaign, related_name='files', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.file.name

from django.db import models
from django.contrib.auth.models import User


class Campaign(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    # owner = models.ForeignKey(User, related_name='campaigns', on_delete=models.CASCADE) 

    def __str__(self):
        return self.name


class NPC(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='npcs', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    role = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='events', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Villain(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='villains', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    evil_plan = models.TextField()

    def __str__(self):
        return self.name


class Location(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='locations', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_discovered = models.BooleanField(default=False)

    def __str__(self):
        return self.name
