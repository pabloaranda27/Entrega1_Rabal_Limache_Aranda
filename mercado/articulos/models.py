from django.db import models

class Articles(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    description=models.CharField(max_length=200, null=True, blank=True)
    is_available=models.BooleanField(default=True)
    creation_date=models.DateField(auto_now_add=True, null=True, blank=True)
    stock=models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Article'
        verbose_name_plural='Articles'