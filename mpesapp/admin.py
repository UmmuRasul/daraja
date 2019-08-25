from django.contrib import admin
from mpesapp.models import LNMOnline

# Register your models here.

#admin.site.register(LNMOnline)


class LNMOnlineAdmin(admin.ModelAdmin):
    list_display = ('Phone_number', 'MpesaReceiptNumber', 'Amount', 'Transaction_date')

admin.site.register(LNMOnline, LNMOnlineAdmin)