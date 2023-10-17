from rest_framework import serializers

from library.book_renter.models import BookRenter
from library.validators import phone_number_valid


class ListBookRenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRenter
        fields = ['name', 'address', 'phone_number', 'email']

    def validate(self, data):
        if not phone_number_valid(data['phone_number']):
            raise serializers.ValidationError({'phone_number': "invalid phone number, eleven digits must be"})

        # if not name_valid(data['name']):
        # raise serializers.ValidationError({'name':"The name must contain only alphabetic characters"})

        return data
