from django import forms


class WebuiForm(forms.Form):

    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False
    )
    webui_props = forms.CharField(
        label='WEBUI Props',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False
    )

class MethodRoutingForm(forms.Form):
    is_bank_id_exact_match = forms.ChoiceField(
        label='Is bank id exact match?',
        choices= (
            ('true', 'Yes'),
            ('false', 'No'),
        ),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        initial='',
        required=False,
    )
    method_name = forms.CharField(
        label='Method Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False
    )
    connector_name = forms.CharField(
        label='Connector Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False
    )
    bank_id_pattern = forms.CharField(
        label='Bank id pattern',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False
    )