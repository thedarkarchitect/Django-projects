import django_filters
from django_filters import DateFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')#gte -> greater or equal to, this field will be new and will check for dates that are all greater the date entered
    end_Date = DateFilter(field_name="date_created", lookup_expr='lte')#gte -> lesser or equal to, this field will check for all date that are less or equal to date entered 
    class Meta:
        model = Order
        fields = ['product', 'status']
        # exclude = ['customer', 'date_created']