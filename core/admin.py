from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from tables.core.models import (
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
        'reservation_date', 'table'
    )
    inlines = (TableInline,)

    """ 
    TODO: for custom template with front-end features uncomment this line
    """
    #change_list_template = 'reservation.html'