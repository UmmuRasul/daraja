from rest_framework import serializers
from mpesapp.models import LNMOnline, C2BPayments

class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMOnline
        fields = ['id']

class C2BPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = C2BPayments
        fields = ['id', 'TransactionID', 'TransactionTime', 'TransactionAmount', 'BusinessShortCode', 'BillRefNumber', 'InvoiceNumber', 'OrganisationAcountBalance', 'ThirdPartyTransID', 'MSISDN','FirstName', 'MiddleName','LastName']