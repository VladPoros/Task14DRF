from celery import shared_task
from .models import Author


@shared_task
def change_author_status():
    author_list = Author.objects.filter(is_notified=False).values_list('id', flat=True)

    for author_id in author_list:
        author = Author.objects.get(pk=author_id)
        author.is_notified = True
        author.save()
