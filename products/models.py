from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from unidecode import unidecode


UserModel = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0)])
    quantity = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(to="Category")
    pre_order = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def thumbnail_image_url(self):
        image = self.productimage_set.all()[0]

        return image.image.url

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_details", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            ascii_name = unidecode(self.name)
            self.slug = f"{slugify(ascii_name)}-{self.id}"

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-date_added"]
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images/")


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
