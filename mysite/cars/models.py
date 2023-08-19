from django.db import models

# Create your models here.
class Review(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    review = models.CharField(max_length=500)
    rating = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.first_name}_{self.last_name} has email: "{self.email}" reviewed us: "{self.review}" with rating: "{self.rating}"'