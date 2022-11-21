from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

FLAG_OPTION = (
    ('Hot Coffee', 'Hot Coffee'),
    ('Hot Tea', 'Hot Tea'),
    ('Hot Drink', 'Hot Drink'),
    ('Cold Coffee', 'Cold Coffee'),
    ('Iced Tea', 'Iced Tea'),
    ('Cold Drink', 'Cold Drink'),
    ('Hot Breakfast', 'Hot Breakfast'),
    ('Bakery', 'Bakery'),
    ('Lunch', 'Lunch'),
    ('Snacks&Sweets', 'Snacks&Sweets'),
)

class Product(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    desc = models.TextField(_('Description'), max_length=10000)
    price = models.DecimalField(_('Price'), max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    is_active = models.BooleanField(_('Activated'), default=True)
    publish_date = models.DateTimeField(_('Date Of Publish'), default=timezone.now)
    flag = models.CharField(_('Flag'), max_length=20, choices=FLAG_OPTION)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-publish_date']
