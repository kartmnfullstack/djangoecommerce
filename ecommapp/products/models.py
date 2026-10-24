from django.db import models

class Category(models.Model):

    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Products(models.Model):
    name = models.CharField(max_length=500)
    cat = models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='products/',blank=True,null=True)

    def __str__(self):
        return self.name
