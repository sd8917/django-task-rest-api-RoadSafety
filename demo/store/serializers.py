from rest_framework import serializers
from store.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product #model we want to serialize 
        fields = ['id', 'name', 'description','price', 'sale_start','sale_end'] #field we want to serialize

    #to override and add extra fields

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['is_on_sale'] = instance.is_on_sale()
        data['current_price'] = instance.current_price()
        return data

