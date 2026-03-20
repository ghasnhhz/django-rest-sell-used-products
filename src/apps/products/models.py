from django.db import models

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='sold_products')
    buyer = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
