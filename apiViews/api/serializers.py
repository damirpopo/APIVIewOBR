from rest_framework import serializers

from .models import Cart

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    total_cost= serializers.IntegerField()
    class Meta:
        model = Cart
        fields = '__all__'


def update(self,instance,validated_data):
    instance.name = validated_data.get("name", instance.name)
    instance.total_cost= validated_data.get("total_cost", instance.total_cost)
    instance.save()
    return instance