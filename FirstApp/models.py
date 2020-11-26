from django.db import models

# Create your models here.
class Musician(models.Model):
    #id=models.AutoField(Primary_key=True) #django set it autometically if we not set it
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'

class Album(models.Model):
    artist= models.ForeignKey(Musician,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    rating = (
    (1,'worst'),
    (2,'bad'),
    (3,'Not bad'),
    (4,'good'),
    (5,'Excellent')
    )
    num_stars = models.IntegerField(choices=rating)

    def __str__(self):
        return f'{self.name}   -   Rating: {self.num_stars}'
