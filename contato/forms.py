from django import forms


class ContatoFrom(forms.Form):
    seu_nome = forms.CharField(label="Seu nome", max_length=100, required=True)
    seu_telefone = forms.CharField(label="Seu telefone", max_length=20, required=True)
    seu_email = forms.EmailField(label="Seu email", required=True)
    sua_mensagem = forms.CharField(label="Sua mensagem", max_length=355)