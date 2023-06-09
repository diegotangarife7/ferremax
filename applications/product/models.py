from django.db import models
from django.utils.text import slugify




class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='nombre', unique=True)
    description = models.TextField(null=True, blank=True, verbose_name='descripcion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    image = models.ImageField(upload_to='category', null=True, blank=True, verbose_name='imagen')
    slug = models.SlugField(max_length=50, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categorias'
        verbose_name='categoria'
        verbose_name_plural = 'categorias'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='nombre', unique=True)
    description = models.TextField(verbose_name='descripcion')
    price = models.DecimalField(decimal_places=3, max_digits=12, verbose_name='precio')
    discounted_price = models.DecimalField(decimal_places=3, max_digits=12, default=0, verbose_name='precio con descuento incluido')
    principal_image = models.ImageField(upload_to='products', verbose_name='imagen principal')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    categories = models.ManyToManyField(Category, verbose_name='categorias')
    slug = models.SlugField(max_length=50, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'productos'
        verbose_name='producto'
        verbose_name_plural = 'productos'


class ProductImages(models.Model):
    images = models.ImageField(upload_to='products', verbose_name='imagenes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images') 

    
        

class PrincipalProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='producto de portada')
    new_product = models.BooleanField(default=False, verbose_name='Producto nuevo')

    class Meta:
        db_table='producto principal'
        verbose_name_plural = 'producto principal (inicio)'

    def __str__(self):
        return self.product.name

    

    
