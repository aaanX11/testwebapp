from django import forms

from .models import Supply, Suggestion

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ('items','source','date','latitude','longitude',)
class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ('items','id_user','date','latitude','longitude',)
