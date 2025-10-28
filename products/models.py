from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    ACTIVE = 'active'
    INACTIVE = 'inactive'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'inactive'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=Category.STATUS_CHOICES, default=Category.ACTIVE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class ProductSKU(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='skus')
    screen_size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    hard_disk = models.CharField(max_length=100, null=True, blank=True)
    cpu_model = models.CharField(max_length=100, null=True, blank=True)
    ram = models.CharField(max_length=100, null=True, blank=True)
    graphics_card = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, choices=Category.STATUS_CHOICES, default=Category.ACTIVE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - SKU {self.id}"


class ProductImage(models.Model):
    sku = models.ForeignKey(ProductSKU, on_delete=models.CASCADE, related_name='images')
    image1 = models.ImageField(upload_to='sku_images/')
    image2 = models.ImageField(upload_to='sku_images/')
    image3 = models.ImageField(upload_to='sku_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Images for SKU {self.sku.id}"