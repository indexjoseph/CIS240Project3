from django.urls import path

from . import views
app_name = 'budget_app'
urlpatterns = [
    
    #Index page
    path('', views.index, name = "index"),
    path('transactions/', views.transactions, name='transactions'),
    path('transactions/<int:transaction_id>/', views.transaction, name='transaction'),
]