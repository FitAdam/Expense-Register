from django.db import models

# Create your models here.
class Expense(models.Model):
    """A basic expense"""
    date_added = models.DateTimeField(auto_now_add=True)
    type_used = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    amount = models.FloatField()
    currency = models.CharField(default='€', max_length=2)


    def __str__(self):
        """Return a string representation of the model."""
        return self.company_name


