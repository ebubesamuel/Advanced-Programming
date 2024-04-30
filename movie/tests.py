from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from movie.models import Movie, Review, Likes

class LikesModelTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.movie = Movie.objects.create(Title='Test Movie')
        self.review = Review.objects.create(user=self.user, movie=self.movie, text='Test Review', rate=7)
        self.like = Likes.objects.create(user=self.user, type_like=1, review=self.review)

    def test_like_creation(self):
        like_count = Likes.objects.count()
        self.assertEqual(like_count, 1)

    def test_like_user(self):
        self.assertEqual(self.like.user, self.user)

    def test_like_type(self):
        self.assertEqual(self.like.type_like, 1)

    def test_like_review(self):
        self.assertEqual(self.like.review, self.review)

    def test_like_creation_negative(self):
        like_count = Likes.objects.count()
        self.assertNotEqual(like_count, 2)

    def test_like_user_negative(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpass')
        self.assertNotEqual(self.like.user, other_user)

    def test_like_type_negative(self):
        self.assertNotEqual(self.like.type_like, 2)

    def test_like_review_negative(self):
        other_review = Review.objects.create(user=self.user, movie=self.movie, text='Other Review', rate=5)
        self.assertNotEqual(self.like.review, other_review)
