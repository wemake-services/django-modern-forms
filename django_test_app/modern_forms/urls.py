from django.urls import path

from django_test_app.modern_forms.views import ContactFormView

app_name = 'modern_forms'

urlpatterns = [
    path('', ContactFormView.as_view(), name='contact_form'),
]
