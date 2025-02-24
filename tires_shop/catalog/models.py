from django.db import models


class Brand(models.Model):
    """
    Бренд шин.
    """
    name = models.CharField(max_length=100, unique=True,
                            verbose_name = "Название бренда")

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
    name = models.CharField(max_length=255, verbose_name="Наименование")
    diameter = models.DecimalField(max_digits=4, decimal_places=1,
                                   verbose_name="Диаметр")
    width = models.IntegerField(verbose_name="Ширина")
    height = models.IntegerField(verbose_name="Высота профиля")
    season = models.CharField(
        choices=[('summer', 'Летние'), ('winter', 'Зимние'),
                 ('allseason', 'Всесезонные')], max_length=10,
        verbose_name = "Сезон")

    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name = "Цена")
    stock = models.IntegerField(verbose_name = "Остатки")  # Остатки
    image = models.ImageField(upload_to='tires/', null=True, blank=True,
                              verbose_name = "Изображение")

    def __str__(self):
        return f"{self.brand.name} {self.name} {self.diameter} {self.season}"
