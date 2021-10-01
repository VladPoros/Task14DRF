from django.core.management.base import BaseCommand
from faker import Faker
from tutorial.quickstart.models import *


class Command(BaseCommand):
    help = 'Adding posts in blog'

    def add_arguments(self, parser):
        parser.add_argument(
            '-q',
            '--quantity',
            type=int,
            default=10,
            help="enter needs quantity of posts"
        )

    def handle(self, *args, **options):
        fake = Faker('ru-RU')
        self.stdout.write('Start inserting posts...')

        for _ in range(options['quantity']):

            author = Author.objects.filter(pk=1)
            if not author:
                author = Author(
                    author_name='test',
                    email='test@test.com',
                    is_notified=False,
                )
                author.save()
                author = Author.objects.filter(pk=1)

            category = Category.objects.filter(pk=1)

            if not category:
                category = Category(category_name='test_category')
                category.save()
                category = Category.objects.filter(pk=1)

            post = Post(author=author[0], categories=category[0])
            post.post_text = fake.sentence(nb_words=10)
            post.pub_date = timezone.now()
            post.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully inserted {options['quantity']} posts..."))
