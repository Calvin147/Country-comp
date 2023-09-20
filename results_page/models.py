from django.db import models

class CountryVote(models.Model):
    """
    Represents a country and the number of votes it has received.

    Attributes:
        country_name (str): The name of the country, limited to 100 characters.
        votes (int): The number of votes received by the country, defaults to 0.

    Methods:
        __str__(): Returns a string representation of the country's name.
    """
    
    country_name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.country_name
    
