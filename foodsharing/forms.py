from django import forms

from .models import Supply, UserSuggestion

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ('source','date','latitude','longitude',)
class SuggestionForm(forms.ModelForm):
    class Meta:
        model = UserSuggestion
        fields = ('user_id','supply','date','latitude','longitude',)
