from typing import final

from django import forms

from django_modern_forms.pydantic import PydanticForm
from django_test_app.modern_forms.dtos import ContactDTO


@final
class ContactForm(PydanticForm[ContactDTO]):
    """Form for contact information."""

    name = forms.CharField()
    age = forms.IntegerField()
