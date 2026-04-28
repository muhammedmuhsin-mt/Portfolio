from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    imge=models.ImageField(upload_to='project_image/')

    def __str__(self):
        return self.title