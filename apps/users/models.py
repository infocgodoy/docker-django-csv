from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'

class MasterProductsConfigurable(models.Model):
    model = models.TextField(blank=True, null=True)
    group_by_model = models.TextField(blank=True, null=True)
    sku = models.TextField(blank=True, null=True)
    yr_es = models.IntegerField(db_column='YR_es', blank=True, null=True)  # Field name made lowercase.
    yr_fr = models.IntegerField(db_column='YR_fr', blank=True, null=True)  # Field name made lowercase.
    name_single_product = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    qty = models.TextField(blank=True, null=True)
    ean1 = models.FloatField(blank=True, null=True)
    color_group_hex = models.TextField(blank=True, null=True)
    color_child = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    special_price = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    cross_selling = models.TextField(blank=True, null=True)
    cross_selling_cart = models.TextField(blank=True, null=True)
    size_chart = models.TextField(blank=True, null=True)
    image1 = models.TextField(blank=True, null=True)
    image2 = models.TextField(blank=True, null=True)
    image3 = models.TextField(blank=True, null=True)
    image4 = models.TextField(blank=True, null=True)
    image5 = models.TextField(blank=True, null=True)
    image6 = models.TextField(blank=True, null=True)
    image7 = models.TextField(blank=True, null=True)
    image8 = models.TextField(blank=True, null=True)
    image9 = models.TextField(blank=True, null=True)
    application_advice = models.TextField(blank=True, null=True)
    attribute_format_container = models.TextField(blank=True, null=True)
    vegetal_active = models.TextField(blank=True, null=True)
    attribute_container = models.TextField(blank=True, null=True)
    attribute_coverage = models.IntegerField(blank=True, null=True)
    inci = models.TextField(blank=True, null=True)
    variant_icon = models.TextField(blank=True, null=True)
    attribute_face = models.IntegerField(blank=True, null=True)
    attribute_esencia = models.IntegerField(blank=True, null=True)
    attribute_line = models.TextField(blank=True, null=True)
    attribute_hair_type = models.IntegerField(blank=True, null=True)
    attribute_type_perfume = models.IntegerField(blank=True, null=True)
    attribute_effect = models.TextField(blank=True, null=True)
    attribute_texture = models.TextField(blank=True, null=True)
    attribute_type_skin = models.TextField(blank=True, null=True)
    attribute_zone = models.TextField(blank=True, null=True)
    attribute_color = models.TextField(blank=True, null=True)
    attribute_ip_solar = models.TextField(blank=True, null=True)
    attribute_action = models.IntegerField(blank=True, null=True)
    attribute_class = models.TextField(blank=True, null=True)
    attribute_type_product = models.TextField(blank=True, null=True)
    attribute_type_care = models.TextField(blank=True, null=True)
    attribute_need = models.TextField(blank=True, null=True)
    category_1_1 = models.TextField(blank=True, null=True)
    category_1_2 = models.IntegerField(blank=True, null=True)
    category_1_3 = models.IntegerField(blank=True, null=True)
    category_2_1 = models.TextField(blank=True, null=True)
    category_2_2 = models.IntegerField(blank=True, null=True)
    category_2_3 = models.IntegerField(blank=True, null=True)
    category_3_1 = models.TextField(blank=True, null=True)
    category_3_2 = models.IntegerField(blank=True, null=True)
    category_3_3 = models.IntegerField(blank=True, null=True)
    category_4_1 = models.TextField(blank=True, null=True)
    category_4_2 = models.IntegerField(blank=True, null=True)
    category_4_3 = models.IntegerField(blank=True, null=True)
    category_5_1 = models.TextField(blank=True, null=True)
    category_5_2 = models.TextField(blank=True, null=True)
    category_5_3 = models.TextField(blank=True, null=True)
    category_6_1 = models.TextField(blank=True, null=True)
    category_6_2 = models.TextField(blank=True, null=True)
    category_6_3 = models.TextField(blank=True, null=True)
    category_7_1 = models.TextField(blank=True, null=True)
    category_7_2 = models.IntegerField(blank=True, null=True)
    category_7_3 = models.IntegerField(blank=True, null=True)
    category_8_1 = models.TextField(blank=True, null=True)
    category_8_2 = models.IntegerField(blank=True, null=True)
    category_8_3 = models.IntegerField(blank=True, null=True)
    category_9_1 = models.TextField(blank=True, null=True)
    category_9_2 = models.IntegerField(blank=True, null=True)
    category_9_3 = models.IntegerField(blank=True, null=True)
    category_10_1 = models.TextField(blank=True, null=True)
    category_10_2 = models.IntegerField(blank=True, null=True)
    category_10_3 = models.IntegerField(blank=True, null=True)
    category_11_1 = models.TextField(blank=True, null=True)
    category_11_2 = models.IntegerField(blank=True, null=True)
    category_11_3 = models.IntegerField(blank=True, null=True)
    category_12_1 = models.TextField(blank=True, null=True)
    category_12_2 = models.IntegerField(blank=True, null=True)
    category_12_3 = models.IntegerField(blank=True, null=True)
    category_13_1 = models.TextField(blank=True, null=True)
    category_13_2 = models.IntegerField(blank=True, null=True)
    category_13_3 = models.IntegerField(blank=True, null=True)
    category_14_1 = models.TextField(blank=True, null=True)
    category_14_2 = models.IntegerField(blank=True, null=True)
    category_14_3 = models.IntegerField(blank=True, null=True)
    attribute_beauty = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    REQUIRED_FIELDS = ['name','sku','price']

    def __str__(self):
        return f'{self.name} {self.sku}'