from rest_framework import serializers
from .models import ToDoItem

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = '__all__'
    
    def create(self, validated_data):
        # Здесь важно получить user из контекста запроса, а не из validated_data
        user = self.context['request'].user
        if user is None or user.is_anonymous:
            raise serializers.ValidationError("User is not authenticated") # Или другая подходящая обработка
        item = ToDoItem.objects.create(
            author=user, # Используем user из контекста запроса
            title=validated_data.get('title'),
            text=validated_data.get('text'),
            completed=validated_data.get('completed'),
            priority=validated_data.get('priority')
        )
        return item
    
    def update(self, instance, validated_data): # Переименован метод на update
        instance.title = validated_data.get('title', instance.title) # Используем get с default значением
        instance.text = validated_data.get('text', instance.text)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.save()
        
        return instance
        