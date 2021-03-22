from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import (
    Hall, Table, Reservation,
)


class TableInline(admin.TabularInline):
    model = Table
    extra = 0


""" Hall admin panel for initial input and update of hall data"""
@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'width', 'length',
    )

""" Table admin panel for table data initial input and update """
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):

    list_display = (
        'number', 'placements', 'shape', 'width', 'length',
        'xlocation', 'ylocation', 'hall'
    )

""" Page for work with custom template implementation """
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'table', 'client_name', 'email', 'phone', 'comment',
        'reservation_date', 'get_table'
    )

    def get_table(self, obj):
        return obj.table
    get_table.short_description = 'Table'
    get_table.admin_order_field = 'reservation__table'

    """ 
    TODO:
    1. Fill template 
    2. Uncomment line below
    """
    #change_list_template = 'reservation.html'