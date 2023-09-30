from django import forms


class OrderForm(forms.Form):
   name = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'css_input'}))
   phone = forms.CharField(max_length=15)


class NewOrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))  # второй аргумент как-то связан с Bootstrap
    phone = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))

