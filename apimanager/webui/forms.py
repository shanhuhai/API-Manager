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
