from django.db import models
from UserServices.models import Users

# Create your models here.

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.TextField()
    description = models.TextField()
    display_order = models.IntegerField(blank=True, null=True)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.JSONField()
    description = models.TextField()
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)