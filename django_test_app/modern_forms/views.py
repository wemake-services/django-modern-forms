from typing import final

from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from django_test_app.modern_forms.forms import ContactForm


@final
class ContactFormView(FormView[ContactForm]):
    """View for displaying and processing contact form."""

    form_class = ContactForm
    template_name = 'modern_forms/contact_form.html'
    success_url = reverse_lazy('modern_forms:contact_form')
