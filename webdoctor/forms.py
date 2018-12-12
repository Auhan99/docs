# useless now

from django.forms import ModelForm
from webdoctor.models import DocHistory

class HistoryForm(ModelForm):
    class Meta:
        model = DocHistory
        fields = ['name', 'age', 'gender', 'phone', 'payment','date']