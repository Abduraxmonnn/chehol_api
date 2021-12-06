from datetime import datetime

from django.db import models


class News(models.Model):

    SALE = 'SALES'
    NEW_PRODUCTS = 'NEW PRODUCTS'

    CATEGORY_NEWS = (
        (SALE, 'SALES'),
        (NEW_PRODUCTS, 'NEW PRODUCTS')
    )

    theme = models.CharField(max_length=100)
    description = models.TextField()
    category_news = models.CharField(max_length=15, choices=CATEGORY_NEWS)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    created_date = models.DateField(default=datetime.now)
    created_time = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'news'

    def __str__(self):
        return f'{self.theme}, {self.image}, {self.created_date}'
