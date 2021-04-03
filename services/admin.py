from django.contrib import admin
from .models import bookForm, registerForm
from root.admin import CustomModelAdmin
# Register your models here.

class bookAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email',
                  'phone_number',
                    'message',
                  'created_at'
        ]
    class Meta:
        model = bookForm

class registerAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email',
                  'phone_number',
                  'cource','message',
                  'created_at'
        ]
    class Meta:
        model = registerForm



admin.site.register(bookForm, bookAdmin)
admin.site.register(registerForm, registerAdmin)

