from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn', 'price')

        def validate(self, data):
            title = data.get('title', None)
            author = data.get('author', None)

            if not title.isalpha():
                raise ValidationError(
                    {
                        'status':False,
                        'massage': "Kitob sarlavhasi satir bo'lishi kerak"
                    }
                )

            if Book.objects.filter(title=title, author=author):
                raise ValidationError(
                    {
                        'status':False,
                        'massage':"Muallif va kitob sarlavhasi birhil bo'lishi mumkin emas"
                    }
                )
            return data