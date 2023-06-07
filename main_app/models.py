from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

LANGUAGES = (
  ('H', 'HTML5'),
  ('C', 'CSS'),
  ('J', 'JavaScript'),
  ('P', 'Python'),
)

# Create your models here.
class Code(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  language = models.CharField(
    max_length=1,
    choices=LANGUAGES,
    default=LANGUAGES[0][0])
  code = models.TextField(max_length=500)
  github = models.URLField(
    max_length=200,
    default="https://www.youtube.com/watch?v=b4jwe4TcqIw&ab_channel=BenManley")
  star = models.BooleanField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("code-detail", kwargs={"code_id": self.id})
  