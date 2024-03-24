from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)


    def __str__(self):
        return self.name


class Shop(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="shop/images")
    slug = models.CharField(max_length=250)
    price = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
