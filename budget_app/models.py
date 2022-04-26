from django.db import models

# Transaction Class
class Transaction(models.Model):

    TransactionType = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.TransactionType)

# Entry Class
class Entry(models.Model):
    
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    merchant = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    transaction_amount = models.FloatField(max_length=10)
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        return str(self.merchant[:50]+"...")