from rest_framework import serializers

from .models import bookForm, registerForm


class bookFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookForm
        fields = ['firstname', 'lastname', 'email',
                  'phone_number',
                  'message',
                  'created_at'
        ]

class registerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = registerForm
        fields = ['firstname', 'lastname', 'email',
                  'phone_number',
                  'cource','message',
                  'created_at'
        ]
