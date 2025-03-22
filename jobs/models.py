from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview Scheduled'),
        ('offered', 'Job Offered'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    application_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    notes=models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.job_title} at {self.company_name} - {self.get_status_display()}"