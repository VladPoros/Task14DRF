from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Post, Category, Comment
from rest_framework import status
import coverage

cov = coverage.Coverage()
cov.start()

client = APIClient()


class PostTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='12345')
        self.user_token = Token.objects.create(user=self.user)

        self.category = Category.objects.create(category_name='Lesson')

        self.correct_post = {
            'post_text': 'Any post',
            'categories': 1,
        }

        self.wrong_post = {
            'post_text': "",
            'categories': 1,
        }

        self.correct_comment = {
            "comment_text": "Any comment",
            "post": 1,
        }

        self.wrong_comment = {
            "comment_text": "",
            "post": 1,
        }

        Post.objects.create(
            post_text="English",
            categories=self.category,
        )

    def test_post_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)

        response = self.client.get('/api/post/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)

    def test_create_correct_post(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)

        response = self.client.post(
            '/api/post/',
            self.correct_post,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_create_wrong_post(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)

        response = self.client.post(
            '/api/post/',
            self.wrong_post,
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Post.objects.count(), 1)

    def test_create_correct_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)

        response = self.client.post(
            '/api/comment/',
            self.correct_comment,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get().comment_text, "Any comment")

    def test_create_wrong_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)

        response = self.client.post(
            '/api/comment/',
            self.wrong_comment,
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Comment.objects.count(), 0)


cov.stop()
cov.save()
cov.html_report()
