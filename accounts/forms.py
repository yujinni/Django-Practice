from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='사용자 이름',
        widget=forms.TextInput(
            attrs={
            'class': 'my-title',
            'placeholder': 'Enter the title',
            'maxlength': 10,
            }
         )
    )
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')



class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'username', 'password')