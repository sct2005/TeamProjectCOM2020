from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from exhibits.models import Exhibit, Comment, Quiz, QuizScore

class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alice", password="password123")
        self.client.login(username="alice", password="password123")

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
        resp = self.client.post(url, data={"body": "Hello"})
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Comment.objects.count(), 1)
        c = Comment.objects.first()
        assert c is not None
        self.assertEqual(c.exhibit_id, self.exhibit.id)
        self.assertIsNone(c.parent_id)
        self.assertEqual(c.user, self.user)
        self.assertEqual(c.author_name, "alice")
        self.assertEqual(c.body, "Hello")

    def test_post_reply_comment(self):
        parent = Comment.objects.create(
            exhibit=self.exhibit,
            user=self.user,
            author_name="Bob",
            body="Parent",
        )
        url = reverse("exhibits:post_comment", args=[self.exhibit.id])
        resp = self.client.post(
            url,
            data={"body": "Reply", "parent_id": str(parent.id)},
        )
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Comment.objects.count(), 2)
        reply = Comment.objects.exclude(id=parent.id).get()
        self.assertEqual(reply.parent_id, parent.id)
        self.assertEqual(reply.user, self.user)

    def test_post_comment_missing_fields_is_400(self):
        url = reverse("exhibits:post_comment", args=[self.exhibit.id])
        resp = self.client.post(url, data={"body": ""})
        self.assertEqual(resp.status_code, 400)

    def test_requires_login_for_comment(self):
        self.client.logout()
        url = reverse("exhibits:post_comment", args=[self.exhibit.id])
        resp = self.client.post(url, data={"body": "Hello"})
        # Should redirect to login
        self.assertEqual(resp.status_code, 302)
        self.assertIn(reverse("login"), resp.url)


class QuizScoreTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="bob", password="password123")
        self.exhibit = Exhibit.objects.create(
            title="Quiz Exhibit",
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
        self.quiz = Quiz.objects.create(
            exhibit=self.exhibit,
            question="Q1?",
            options=["A", "B"],
            correct_answer_index=0,
            explanation="Because.",
        )

    def test_quiz_score_persists_and_keeps_best(self):
        self.client.login(username="bob", password="password123")
        url = reverse("exhibits:quiz", args=[self.exhibit.id])

        # First attempt: 0 correct
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        # Extract order mapping from rendered page
        # Simpler: just post assuming mapping [0,1] (no options shuffling uniqueness checked here)
        resp = self.client.post(
            url,
            data={
                f"answer_{self.quiz.id}": "1",  # wrong index
                f"order_{self.quiz.id}": "[0,1]",
            },
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "exhibits/quiz_results.html")
        self.assertEqual(QuizScore.objects.count(), 1)
        score = QuizScore.objects.get()
        self.assertEqual(score.correct_answers, 0)

        # Second attempt: correct answer, should update best score
        resp = self.client.post(
            url,
            data={
                f"answer_{self.quiz.id}": "0",  # correct
                f"order_{self.quiz.id}": "[0,1]",
            },
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(QuizScore.objects.count(), 1)
        score.refresh_from_db()
        self.assertEqual(score.correct_answers, 1)
