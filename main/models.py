from django.db import models


class region(models.Model):
    title = models.CharField('Название района', max_length=255)
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'Название районов'
        verbose_name_plural = 'Название районов'


class estate(models.Model):
    count_room = models.CharField('Кол-во комнат', max_length=255)
    floor = models.CharField('Этаж', max_length=255)
    square_meters = models.CharField('Метраж', max_length=255)
    price = models.FloatField('Цена', max_length=255)
    region = models.ForeignKey(region, on_delete=models.CASCADE, blank=True, null=True)
    cover = models.ImageField(upload_to='images/')


    def __str__(self):
        return f'{self.count_room} ком. кв.'

    class Meta:
        verbose_name = 'Картотека недвижимости'
        verbose_name_plural = 'Картотека недвижимости'
