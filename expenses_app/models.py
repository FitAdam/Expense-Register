from django.db import models
from django.forms import ModelForm

CURRENCY_CHOICES = [('£','£'),('$','$'),('€','€')]
CURRENCY_TYPE = [('Cash', 'cash'), ('Card', 'card')]

class Expense(models.Model):
    """A basic expense"""
    date_added = models.DateTimeField(auto_now_add=True)
    type_used = models.CharField(max_length=32, choices=CURRENCY_TYPE, default='card')
    company_name = models.CharField(max_length=100)
    amount = models.FloatField()
    currency = models.CharField(default='€', max_length=16, choices=CURRENCY_CHOICES)


    def __str__(self):
        """Return a string representation of the model."""
        return self.company_name


