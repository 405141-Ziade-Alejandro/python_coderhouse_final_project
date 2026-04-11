from django.db import models

# Create your models here.



class State(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

class WorkStation(models.Model):
    code = models.IntegerField(unique=True)
    origin_area= models.CharField(max_length=50)
    description = models.TextField()
    date_received = models.DateField(auto_now_add=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    ws_user = models.CharField(max_length=50)

    def __str__(self):
        return f"WS{self.code}"

class SuppliesType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Supply(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(SuppliesType, on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.IntegerField()
    description = models.TextField()
    location = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.description}; tenemos un stock de {self.stock}"