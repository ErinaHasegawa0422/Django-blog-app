from django.test import TestCase
from .models import Post, Comment
from django.utils import timezone

class PostCommentTest(TestCase):
    def setUp(self):
        # Postのインスタンスを作成
        self.post = Post.objects.create(
            title="Sample Post",
            slug="sample-post",
            intro="Introduction of the sample post",
            body="Body of the sample post",
            posted_data=timezone.now()
        )
        
        # Commentのインスタンスを作成
        self.comment = Comment.objects.create(
            post=self.post,
            name="John Doe",
            email="john@example.com",
            body="This is a sample comment",
            posted_data=timezone.now()
        )

    def test_post_fields(self):
        post = self.post
        self.assertEqual(post.title, "Sample Post")
        self.assertEqual(post.slug, "sample-post")
        self.assertEqual(post.intro, "Introduction of the sample post")
        self.assertEqual(post.body, "Body of the sample post")

    def test_comment_fields(self):
        comment = self.comment
        self.assertEqual(comment.name, "John Doe")
        self.assertEqual(comment.email, "john@example.com")
        self.assertEqual(comment.body, "This is a sample comment")
        self.assertEqual(comment.post, self.post)

    def test_post_comment_relation(self):
        post = self.post
        # Postに紐付けられたCommentが正しく取得できるか
        self.assertEqual(post.comments.count(), 1)
        self.assertEqual(post.comments.first(), self.comment)
