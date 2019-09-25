from django import forms 
form .models import Article 

class ArticleModelForm(forms.Modelform):
    class Meta:
        model = Article
        fields ={
            'title',
            'content',
            'active',
            'type_of_novel',
            'publish_date',
            'email'
        }