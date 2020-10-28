from django import forms

from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['type_used', 'company_name', 'amount', 'currency']
        labels = {'type_used': 'Cash or Cards', 'company_name': 'Company name','amount': 'amount', 'currency': 'Choose your currency' }
