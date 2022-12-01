from django import forms


class LoginForm(forms.Form):
    username  = forms.CharField(max_length = 150)
    password  = forms.CharField(
        widget=forms.PasswordInput()                 
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600'
    
