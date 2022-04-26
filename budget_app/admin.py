from django.contrib import admin
from budget_app.models import Entry, Transaction

admin.site.register(Transaction)
admin.site.register(Entry)
# Register your models here.
