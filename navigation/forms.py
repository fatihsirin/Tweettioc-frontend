from django import forms
from .models import Contribute
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class ContributeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContributeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields["content"].widget.attrs["rows"] = "10"
        self.fields["content"].widget.attrs["cols"] = "100"


    class Meta:
        model = Contribute
        fields = ("content","message_type")
        labels = {
            'content': 'Message',
        }

