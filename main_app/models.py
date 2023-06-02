from django.db import models
from django.urls import reverse

# Create your models here.
class Code(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  code = models.TextField(max_length=500)
  github = models.CharField(max_length=100)
  star = models.BooleanField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("code-detail", kwargs={"code_id": self.id})
  