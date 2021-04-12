from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
# Create your models here.

class MasterProductsConfigurable(models.Model):

    model = models.TextField(blank=True, null=True)
    group_by_model = models.TextField(blank=True, null=True)
    sku =  models.CharField(max_length = 255,primary_key = True)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)

    class Meta:

        
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):

        return self.model