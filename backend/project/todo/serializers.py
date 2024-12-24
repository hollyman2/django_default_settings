from rest_framework import serializers
from .models import ToDoItem

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = '__all__'
    
    def create(self, user, validated_data):
        item= ToDoItem.objects.create(
            author=user,
            title=validated_data.get('title'),
            text=validated_data.get('text'),
            completed= validated_data.get('completed'),
            priority=validated_data.get('priority')
        )
        return ToDoSerializer(item)
    
    def edit(self, validated_data, item):
        
        if validated_data.get('title'):
            item.title = validated_data.get('title')
        if validated_data.get('text'):
            item.title = validated_data.get('text')
        if validated_data.get('completed'):
            item.title = validated_data.get('completed')
        if validated_data.get('priority'):
            item.title = validated_data.get('priority')

        item.save()
        return ToDoSerializer(item)
        