from django import forms
from news.models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'title'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'description'}))

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "name", "description"]
        labels = {
            "title": "Bashliq",
            "name": "Ad"
        }
        error_messages = {
            'title': {
                'required': 'Vacibdir'
            }
        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = field

    def equalizer(self):
        if self.cleaned_data['title'] == self.cleaned_data['name']:
            return True
        else:
            return False
