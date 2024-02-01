from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description available.")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='webapp/product_images')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductInventory(models.Model):
    product = models.OneToOneField('Product', on_delete=models.CASCADE)
    initial_quantity = models.PositiveIntegerField()
    current_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - In Stock: {self.current_quantity}"

class SalesReport(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    date_generated = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Sales Report for {self.product.name} - Total Sales: {self.total_sales}"

class ProductReview(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=255)
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Review for {self.product.name} by {self.reviewer_name} - Rating: {self.rating}"