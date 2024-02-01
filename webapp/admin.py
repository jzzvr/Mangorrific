from django.contrib import admin

# Register your models here.

from .models import Product
from .models import Category
from .models import ProductInventory
from .models import SalesReport
from .models import ProductReview

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductInventory)
admin.site.register(SalesReport)
admin.site.register(ProductReview)
