from django.db import models

class Orders(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='orders_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('Новый', 'Новый'),
        ('Подтверждён', 'Подтверждён'),
        ('В обработке', 'В обработке'),
        ('Отправлен', 'Отправлен'),
        ('Доставлен', 'Доставлен'),
        ('Отменён', 'Отменён'),
    ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Order {self.customer_name} - {self.product_name}"

