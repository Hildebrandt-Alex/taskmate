# yourapp/models.py
from django.db import models

class SiteSettings(models.Model):
    TEMPLATE_CHOICES = [
        ('base1.html', 'navbar 1'),
        ('base2.html', 'navbar 2'),
        ('base3.html', 'navbar 3'),
    ]

    template = models.CharField(
        max_length=100,
        choices=TEMPLATE_CHOICES,
        default='base1.html'
    )

    def __str__(self):
        return f"Navbar choice: {self.template}"
