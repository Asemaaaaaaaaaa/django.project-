from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from project.models import Books,Training1,Training2


class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    photo = serializers.ImageField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.photo = validated_data.get("photo", instance.photo)
        instance.category_id = validated_data.get("category_id", instance.category_id)

        instance.save()
        return instance




# def encode():
#     model = BookModel('book' ,'author','description',4500)
#     model_sr = BookSerializer(model)
#     print(model_sr.data , type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

    # class Meta:
    #     model = Books
    #     fields = ('title' , 'category_id')

class Training1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Training1
        fields = ('title' , 'training_manager')

class Training2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Training2
        fields = ('title' , 'training_manager')