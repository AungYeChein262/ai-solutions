from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100, blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    job_details = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Forms"

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=120)
    job_title = models.CharField(max_length=120)
    company = models.CharField(max_length=160)
    rating = models.PositiveSmallIntegerField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.name} ({self.rating}/5)"


class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="articles/")
    summary = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to="articles/", blank=True, null=True)
    summary = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
