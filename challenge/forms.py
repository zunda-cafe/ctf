from django.forms import ModelForm
from challenge.models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('flag', )
