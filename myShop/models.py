from django.db import models


class Product(models.Model):
    name = models.CharField('Название товара', max_length=50)
    description = models.TextField('Описание товара', blank=True)
    price = models.DecimalField('Цена товара', max_digits=10, decimal_places=2)
    image = models.ImageField('Изображение товара', upload_to='products/', blank=True)
    brand = models.CharField('Бренд товара', max_length=50, blank=True)
    quantity = models.PositiveIntegerField('Количество товара', default=0)
    сreated_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.name} - ${self.price}'

class SerialNumber(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='serial_numbers')
    serial_number = models.CharField('Серийный номер', max_length=100, unique=True)

    def __str__(self):
        return f'{self.product.name} - {self.serial_number}'

class ProductComment(models.Model):
    choice_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    description = models.TextField('Комментарий', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f'Комментарий к {self.choice_product.name} - {self.created_at}'