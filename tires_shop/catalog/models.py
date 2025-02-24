from django.db import models


class Brand(models.Model):
    """
    Бренд шин.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tire(models.Model):
    """
    Модель шины

    Attributes:
        brand (models.ForeignKey): Ссылка на бренд шины.
        name (models.CharField): Название модели шины.
        diameter (models.DecimalField): Диаметр шины.
        width (models.IntegerField): Ширина шины.
        height (models.IntegerField): Высота шины.
        season (models.CharField): Сезонность шины.
        price (models.DecimalField): Цена шины.
        stock (models.IntegerField): Остатки шины на складе.
        image (models.ImageField): Изображение шины.

    Methods:
        __str__(): Возвращает строковое представление объекта в формате "Бренд Модель Диаметр Сезон".
    """
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    diameter = models.DecimalField(max_digits=4, decimal_places=1)
    width = models.IntegerField()
    height = models.IntegerField()
    season = models.CharField(
        choices=[('summer', 'Летние'), ('winter', 'Зимние'),
                 ('allseason', 'Всесезонные')], max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()  # Остатки
    image = models.ImageField(upload_to='tires/', null=True, blank=True)

    def __str__(self):
        return f"{self.brand.name} {self.name} {self.diameter} {self.season}"
