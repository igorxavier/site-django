from django import forms
from django.contrib.auth.models import User
from genericpath import exists


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Repetir Senha'
    )
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput()
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600'
            field.widget.attrs['placeholder'] = field.label
            
            
    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email =email).exists()
        
        if exists:
            raise forms.ValidationError('Esse email já existe na base de dados')
        
        return email
            
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        
        if password != password2:
            raise forms.ValidationError({
                'password': 'O campo senha deve ser repetido',
                'password2': 'Repita o mesmo valor do campo de senha',
            })
    