from django import forms
from .models import Book
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        # fields = ("title", "content")
        exclude = ('metrics',)


    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "test" in title:
            raise ValidationError("Tiltle shouldn't has test word!")
        return title

    def clean(self):
        super(BookForm, self).clean
        content = self.cleaned_data.get("content")
        if len(content) < 10:
            raise ValidationError("Content must be bigger than 10 characters")
        return self.cleaned_data

        
        
