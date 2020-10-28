from django.shortcuts import render, redirect
from django.db.models import Sum


from .models import Expense
from .forms import ExpenseForm

# Create your views here.
def index(request):
    """The home page for Expense Register"""
    expenses = Expense.objects.order_by('date_added')
    context = {'expenses': expenses}
    return render(request, 'expenses_app/index.html', context)

def new_expense(request):
    """Add a new post"""
    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = ExpenseForm()
    else:
        # POST data submitted; process data.
        form = ExpenseForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
            return redirect('expenses_app:index')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'expenses_app/new_expense.html', context)

def analysis(request):
    """This page displays analysis of expenses"""
    labels = []
    data = []

    expenses = Expense.objects.values('company_name').annotate(amount=Sum('amount')).order_by('-amount')
    for entry in expenses:
        labels.append(entry['company_name'])
        data.append(entry['amount'])
    #print(labels)
    #print(data)
    total_sum = round(sum(data),2)
    #print(total_sum)
    context = {'labels': labels, 'data': data, 'total_sum': total_sum}
    return render(request, 'expenses_app/analysis.html', context)