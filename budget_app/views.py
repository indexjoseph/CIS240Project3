from django.shortcuts import render
from . models import Transaction
# Create your views here.
def index(request):
    return render(request, 'budget_app/index.html')

def transactions(request):
    transactions = Transaction.objects.order_by('date_added')
    context = {"transactions" : transactions}
    return render(request, 'budget_app/transactions.html', context)

def transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    entries = transaction.entry_set.ordey_by('date_added')
    context = {'transaction': transaction, 'entries': entries}
    return render(request, 'budget_app/transaction.html', context)

