from django.db import models
from django import forms


class Blog(models.Model):
    text = models.TextField('Текст')
    state = models.BooleanField('Видимость на сайте', default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s ...' % self.text[:20]

    class Meta:
        db_table = 'annonumus_blog'
        verbose_name = 'аннонимный блог'


class FormBlog(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        if text is None:
            self.add_error('text', 'Поле обязательно для заполнения')
        return cleaned_data

    class Meta:
        model = Blog
        fields = ['text',]
        widgets = {
            'text': forms.Textarea(attrs={'rows':13, 'cols':85}),
        }
