from rest_framework import serializers
from .models import Contact, Author, Book

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
        extra_kwargs = {
            "name":{
               "min_length":3,
               "max_length":10,
               "error_messages":{"min_length":"Name must be 3 char long"},
               "error_messages":{"max_length":"Name must not be more than 10 char long"},

            },
            #"address":{"required":False}
        }

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset = Author.objects.all()
    )
    class Meta:
        model = Book
        fields = "__all__"