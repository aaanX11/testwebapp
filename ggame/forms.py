from django import forms

from .models import Riddle

class RiddleForm(forms.ModelForm):
    class Meta:
        model = Riddle
        fields = ('answer',)
    def clean(self):
        print 'forms clean', self.cleaned_data.get('answer')
    def check(self):
        
        obj=super(RiddleForm, self)
        if obj.answer==self.cleaned_data.get('answer'):
            return True
        else:
            return False
        print 'forms check', self.answer
