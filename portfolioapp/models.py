from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_url = models.URLField()
    live_page_url = models.URLField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    date = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='certification_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} by {self.issuer}"
