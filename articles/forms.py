from django.forms.models import inlineformset_factory
from .models import Article, Comment

CommentFormSet = inlineformset_factory(
    Article, Comment, fields=["article", "author", "body"], exclude=[], can_delete=False
)
