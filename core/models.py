from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Event(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title