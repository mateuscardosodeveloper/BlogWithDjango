from django import forms

from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get("title")
        queryset = BlogPost.objects.filter(title__iexact=title) #iexact valid information if have uppercase or not
        if instace is not None:
            qs = qs.exclude(pk=instance.pk) #id=instance.pk
        if queryset.exists():
            raise forms.ValidationError("This title has already been used. Please try again.")
        return title
