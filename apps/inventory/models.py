
from django.db import models
from django.core.validators import MinLengthValidator
from data.custom_fields import CustomAutoField, CustomBooleanField, CustomCharField, CustomIntegerField


class Product(models.Model):
    id = CustomAutoField(primary_key=True, verbose_name="ID", null=False, blank=False, editable=False)
    code = CustomCharField(max_length=10, verbose_name="Code", null=False, blank=False, validators=[MinLengthValidator(3)])
    name = CustomCharField(max_length=100, verbose_name="Nmae", null=False, blank=False)
    description = CustomCharField(max_length=200, verbose_name="Description", null=True, blank=True)
    price = CustomIntegerField(verbose_name="Price", null=False, blank=False)
    stock = CustomIntegerField(verbose_name="Stock", null=False, blank=False)
    archived = CustomBooleanField(verbose_name="Archived", null=False, blank=False, default=True)
    
    def __str__(self):
        return f"{self.code} - {self.name}"
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']
    
    def delete(self):
        # Custom logic to manage relations before delete
        super().delete()