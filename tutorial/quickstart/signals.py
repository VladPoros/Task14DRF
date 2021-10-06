from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import Post, Comment
import re
from profanity_filter import ProfanityFilter


@receiver(pre_save, sender=Post)
def correct_post_without_spec_symbol(sender, instance, *args, **kwargs):
    instance.title = re.sub(r'[^A-Za-zА-Яа-я0-9!?-]', ' ', instance.title)
    #Also we can use this r'[#%^&*()\[\]{}=/+@$_]'


@receiver(pre_save, sender=Comment)
def correct_comment_without_bad_words_EN_RU(sender, instance, *args, **kwargs):

    # Can use Spacy and ProfanityFilter only for EN words
    pf = ProfanityFilter()
    instance.comment_text = pf.censor(instance.comment_text)

    # For Russian words do via code
    list_bad_word = ['плохое_слово1', 'плохое_слово2']
    for bad_word in list_bad_word:
        if bad_word in instance.comment_text:
            instance.comment_text = instance.comment_text.replace(bad_word, str(len(bad_word)*'*'))



@receiver(pre_delete, sender=Comment)
def comment_cancel_delete(sender, instance, *args, **kwargs):
    raise Exception(f'You can not delete comment: {instance.comment_text}')
