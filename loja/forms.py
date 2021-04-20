from django import forms
from .models import Funcionario


class FuncionarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Funcionario
