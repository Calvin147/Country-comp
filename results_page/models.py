from django.db import models

class CountryVote(models.Model):
    country_name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.country_name
    
