from django.db import models


class CoverCategory(models.Model):
    material = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Cover category"
        verbose_name_plural = "cover category"

    def __str__(self):
        return f'{self.material}'


class CarsCategory(models.Model):
    car_name = models.CharField(max_length=50, verbose_name='Car name')
    car_model = models.CharField(max_length=50, blank=True, verbose_name='Car model')

    class Meta:
        verbose_name = 'Car category'
        verbose_name_plural = 'car category'

    def __str__(self):
        return f'{self.car_name}, {self.car_model}'


class Cover(models.Model):
    car_name = models.ManyToManyField(CarsCategory)
    cover = models.ManyToManyField(CoverCategory)
    pattern = models.BooleanField(default=False, blank=False, verbose_name="Cover patterns")
    color = models.CharField(max_length=10, verbose_name="Cover color")
    price = models.IntegerField(verbose_name="Cover price")
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=False, null=True, verbose_name="Picture")
    phone_number = models.CharField(max_length=20, blank=False)
    instagram = models.CharField(max_length=30, blank=False, verbose_name='Instagram link')
    telegram = models.CharField(max_length=30, blank=True, verbose_name='Telegram link')

    class Meta:
        verbose_name = "Covers"
        verbose_name_plural = "covers"

    def __str__(self):
        return f'{self.car_name}, {self.cover}, {self.pattern}, {self.color}, {self.price}. {self.image}, ' \
               f'{self.instagram}, {self.telegram}'
