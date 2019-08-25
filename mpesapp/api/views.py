from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from mpesapp.models import LNMOnline, C2BPayments
from mpesapp.api.serializers import LNMOnlineSerializer, C2BPaymentSerializer


class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = (AllowAny)
    

    def create(self, request):
        print(request.data, 'This is request.data')

        merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
        print(merchant_request_id, 'this is merchant_request_id')

        checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
        result_code = request.data['Body']['stkCallback']['ResultCode']
        result_description = request.data['Body']['stkCallback']['ResultDes']
        amount = request.data['Body']['stkCallback']['CallbackMetadata']['item'][0]['Value']
        print(amount, 'the amount printed')
        mpesa_receipt_number = request.data['Body']['stkCallback']['CallbackMetadata']['item'][1]['Value']
        print(mpesa_receipt_number, 'the amount printed mpesa_receipt_number')

        balance = ''
        transaction_date = request.data['Body']['stkCallback']['CallbackMetadata']['item'][3]['Value']
        print(transaction_date, 'the amount printed transaction_date')

        phone_number = request.data['Body']['stkCallback']['CallbackMetadata']['item'][4]['Value']
        print(phone_number, 'the amount printed phone_number')
        
        from datetime import datetime

        str_transaction_date = str(transaction_date)
        print(str_transaction_date, 'the should printed transaction_date')

        transaction_date_time = datetime.strptime(str_transaction_date, '%Y%m%d%H%M%S')
        print(transaction_date_time, 'the should printed transaction_date_time')


        import pytz

        aware_transaction_datetime = pytz.utc.localized(transaction_date)
        print(aware_transaction_datetime, 'the should printed aware_transaction_datetime')

        
        from mpesapp.models import LNMOnline

        our_model =LNMOnline.objects.create(
            CheckOutRequestID = checkout_request_id,
            MerchantRequestID = merchant_request_id,
            Amount = amount,
            Result_code = result_code,
            ResultDesc = result_description,
            MpesaReceiptNumber = mpesa_receipt_number,
            Balance = balance,
            Transaction_date = aware_transaction_datetime,
            Phone_number = phone_number,
        )
        our_model.save()

        from rest_framework.response import Response

        return Response({'OurResultDesc':'Alhamdulillah!! It worked'})



class C2BValidationAPIView(CreateAPIView):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = (AllowAny)
    

    # def create(self, request):
    #     print(request.data, 'this is request.data in validation')

    #     from rest_framework.response import Response

    #     return Response({'OurResultDesc':'Alhamdulillah!! It worked'})

class C2BConfirmationAPIView(CreateAPIView):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = (AllowAny)
    

    def create(self, request):
        print(request.data, 'this is request.data in Confirmation')

        from rest_framework.response import Response

        return Response({'OurResultDesc':0})