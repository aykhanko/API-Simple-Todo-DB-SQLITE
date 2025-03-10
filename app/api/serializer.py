from rest_framework import serializers
from app.models import Todos

class TodosSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta():
        model = Todos
        fields = '__all__'