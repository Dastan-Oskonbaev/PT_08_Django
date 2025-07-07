from django.db import models

class PlaceCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    short_description = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Place(models.Model):
    category = models.ForeignKey(
        PlaceCategory,
        on_delete=models.CASCADE,
        related_name='places',
    )
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to='places/',
        blank=True,
        null=True
    )
    views_count = models.PositiveIntegerField()
    created_at = models.DateField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'



class Review(models.Model):
    email = models.EmailField()
    fio = models.CharField(
        max_length=100,
    )
    review = models.TextField()
    rating = models.PositiveIntegerField
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )


    def  __str__(self):
        return self.fio


    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

