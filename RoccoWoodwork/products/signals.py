from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Product, ProductImage, Category


@receiver(post_save, sender=Category)
def invalidate_categories_cache(sender, instance, **kwargs):
    cache.delete("categories")


# @receiver(post_save, sender=Product)
# @receiver(post_save, sender=ProductImage)
# def invalidate_cache(sender, instance, **kwargs):
#     cache.clear()
