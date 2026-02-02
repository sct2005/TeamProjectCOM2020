from django.test import TestCase
from django.urls import reverse

from exhibits.models import Exhibit, Comment


class CommentTests(TestCase):
    def setUp(self):
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Test",
            deployment_context="ctx",
            intended_use="use",
            system_type="type",
            inputs_and_assumptions="in",
            outputs_presented="out",
            failure_description="fail",
            detection_method="detect",
            affected_parties="people",
            contributing_factors="factors",
            lessons_learned="lessons",
        )

    def test_post_top_level_comment(self):
        url = reverse("exhibits:post_comment", args=[self.exhibit.id])
        resp = self.client.post(url, data={"author_name": "Alice", "body": "Hello"})
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Comment.objects.count(), 1)
        c = Comment.objects.first()
        assert c is not None
        self.assertEqual(c.exhibit_id, self.exhibit.id)
        self.assertIsNone(c.parent_id)
        self.assertEqual(c.author_name, "Alice")
        self.assertEqual(c.body, "Hello")

    def test_post_reply_comment(self):
        parent = Comment.objects.create(
            exhibit=self.exhibit,
            author_name="Bob",
            body="Parent",
        )
        url = reverse("exhibits:post_comment", args=[self.exhibit.id])
        resp = self.client.post(
            url,
            data={"author_name": "Carol", "body": "Reply", "parent_id": str(parent.id)},
        )
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Comment.objects.count(), 2)
        reply = Comment.objects.exclude(id=parent.id).get()
        self.assertEqual(reply.parent_id, parent.id)

    def test_post_comment_missing_fields_is_400(self):
        url = reverse("exhibits:post_comment", args=[self.exhibit.id])
        resp = self.client.post(url, data={"author_name": "", "body": ""})
        self.assertEqual(resp.status_code, 400)
