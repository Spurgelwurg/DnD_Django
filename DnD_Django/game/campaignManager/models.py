from django.db import models

from django.db import models

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()

    def __str__(self):
        return self.name
    
class NPC(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Enemy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.name