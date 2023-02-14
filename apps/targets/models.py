from django.db import models


class Target(models.Model):
    """
    Model to represent the targets.

    Fields:
        name (str): Name of the target.
        latitude (Decimal): Latitude coordinate of the target.
        longitude (Decimal): Longitude coordinate of the target.
        date of expiry (Date): Expiration date of the target.
    
    Properties:
        location(tuple): The location of the target as a tuple (latitude, longitude).

    Methods:
        __str__(): Returns the target's name as a string.
    """
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    date_expiry = models.DateField()

    @property
    def location(self):
        """
        Returns the location of the target as a tuple (latitude, longitude).
        """
        return (self.latitude, self.longitude)
        
    def __str__(self):
        """
        Returns the target name as a string.
        """
        return self.tree.name
