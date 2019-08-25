# Generated by Django 2.2.4 on 2019-08-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lnmonline',
            name='Amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Balance',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='CheckOutRequestID',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='MerchantRequestID',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='MpesaReceiptNumber',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Phone_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='ResultDesc',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Result_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Transaction_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]