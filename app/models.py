from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    rating = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Forms"

    def __str__(self):
        return f"{self.name} ({self.company})"
