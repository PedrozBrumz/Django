from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    codigo_coordenador = forms.CharField(max_length=4, required=False, label='Código Coordenador')

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'coordenador', 'codigo_coordenador', 'professor')

    def clean_codigo_coordenador(self):
        codigo = self.cleaned_data.get('codigo_coordenador')
        if codigo and codigo != '1234':  # Substitua '1234' pelo código correto
            raise forms.ValidationError("Código inválido para coordenador.")
        return codigo

    def save(self, commit=True):
        user = super().save(commit=False)
        codigo = self.cleaned_data.get('codigo_coordenador')

        # Se o código for válido, marca como coordenador
        if codigo == '1234':  # Substitua com o código correto
            user.coordenador = True
            user.professor = False  # Pode ajustar conforme sua lógica

        if commit:
            user.save()
        return user