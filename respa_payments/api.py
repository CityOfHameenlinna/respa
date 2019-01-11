from django.utils.translation import ugettext_lazy as _
from django.utils.module_loading import import_string
from django.utils import timezone
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework import serializers
from resources.models.resource import Resource
from resources.api.resource import ResourceSerializer
from respa_payments.models import Order, Sku
from respa_payments import settings


class PaymentResourceSerializer(ResourceSerializer):
    class Meta:
        model = Resource
        exclude = ('reservation_requested_notification_extra', 'reservation_confirmed_notification_extra',
                   'access_code_type', 'reservation_metadata_set')


class SkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sku
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderPostView(APIView):
    permission_classes = (permissions.AllowAny,)

    def __init__(self):
        self.payment_integration = import_string(settings.INTEGRATION_CLASS)

    def post(self, request):
        return self.payment_integration(request=request).order_post()


class OrderCallbackView(APIView):
    permission_classes = (permissions.AllowAny,)

    def __init__(self):
        self.payment_integration = import_string(settings.INTEGRATION_CLASS)

    def get(self, request):
        return self.payment_integration(request=request).payment_callback()