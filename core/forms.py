from django import forms


class CheckoutForm(forms.Form):
    address = forms.CharField(
        widget=forms.TextInput
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=False,
        label='یادداشت(اختیاری)'
    )
