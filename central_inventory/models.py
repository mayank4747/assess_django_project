from django.db import models
from django.conf import settings

# ELECTRONICS = "ELECTRONICS"
# BOOKS = "BOOKS"
# COMPUTERS = "COMPUTERS"

# CATEGORY_CHOICES = (
#     (ELECTRONICS, ELECTRONICS),
#     (BOOKS, BOOKS),
#     (COMPUTERS, COMPUTERS),
# )

# class Product(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="product",
#         null=True,
#     )
#     category = models.CharField(
#         max_length=50, choices=CATEGORY_CHOICES,
#     )
#     price = models.DecimalField(
#         max_digits=10, decimal_places=2, null=False, blank=False, default=0.0
#     )
#     name = models.CharField(max_length=50, null=False, blank=False)
#     description = models.TextField(null=True, blank=True)
#     quantity = models.IntegerField(default=0)

class IAP(models.Model):
    site_id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=50,null=False)
    country = models.CharField(max_length=50,null=False)
    order_id = models.IntegerField(null=False)
    purchase_id = models.IntegerField(null=False)
    csm_name = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    macaddr = models.CharField(max_length=30)

