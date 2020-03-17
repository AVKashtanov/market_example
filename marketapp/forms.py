from django import forms
from marketapp.models import Tovar, Sklad, Postavschik, Postavka

class TovarForm(forms.ModelForm):

    class Meta:
        model = Tovar
        fields = '__all__'

class SkladForm(forms.ModelForm):

    class Meta:
        model = Sklad
        fields = '__all__'

class PostavschikForm(forms.ModelForm):

    class Meta:
        model = Postavschik
        fields = '__all__'

class PostavkaForm(forms.ModelForm):

    class Meta:
        model = Postavka
        fields = ('code', 'count_post', 'postavschik')