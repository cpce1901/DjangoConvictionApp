from django import forms

class LoginForm(forms.Form):

    email = forms.EmailField(
        label='Email',
        min_length=4,
        max_length=16,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "id": "email",
                "placeholder": "Ingresar tu correo",
                "class": "text-input"
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        min_length=4,
        max_length=32,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "id": "password",
                "placeholder": "Ingresar contraseña",
                "class": "text-input"
            }
        )
    )