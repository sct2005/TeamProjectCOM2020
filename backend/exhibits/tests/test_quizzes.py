from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from exhibits.models import Exhibit, Quiz, QuizScore, UserProfile

def create_exhibit():
    return Exhibit.objects.create(
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

def create_user(username, access_level):
    user = User.objects.create_user(
        username = username,
        email = username.lower() + "@example.com",
        password = "Password1"
    )

    UserProfile.objects.create(user = user, access_level = access_level)
    return user

def create_quiz(exhibit, question, options, correct, explanation):
    return Quiz.objects.create(
        exhibit = exhibit,
        question = question,
        options = options,
        correct_answer_index = correct,
        explanation = explanation
    )


class QuizTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.exhibit = create_exhibit()
        self.quiz = create_quiz(self.exhibit, "question", ["A", "B", "C"], 0, "because it is")
        self.user = create_user("Alice", "user")
    
    def submit_answer(self, answer_index):
        return self.client.post(reverse("exhibits:quiz", args = [self.exhibit.pk]), {
            f"answer_{self.quiz.id}": str(answer_index),
            f"order_{self.quiz.id}": "[0, 1, 2]",
        })
    
    def test_correct_answer(self):
        self.assertEqual(self.quiz.get_correct_answer(), "A")
    
    def test_deleting_exhibit_also_deletes_quiz(self):
        quiz_id = self.quiz.pk
        self.exhibit.delete()
        self.assertFalse(Quiz.objects.filter(pk = quiz_id).exists())
    
    def test_exhibit_has_multiple_questions(self):
        create_quiz(self.exhibit, "question2", ["A", "B", "C"], 1, "because it is")
        create_quiz(self.exhibit, "question3", ["A", "B", "C"], 2, "because it is")
        self.assertEqual(self.exhibit.quizzes.count(), 3)
    
    def test_submit_correct_answers(self):
        self.client.login(username = "Alice", password = "Password1")
        response = self.client.post(reverse("exhibits:quiz", args = [self.exhibit.pk]), {
            f"answer_{self.quiz.id}": "0",
            f"order_{self.quiz.id}": "[0, 1, 2]",
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1")
        self.assertContains(response, "100")
                                    

    def test_submit_all_wrong_answers(self):
        self.client.login(username = "Alice", password = "Password1")
        response = self.client.post(reverse("exhibits:quiz", args=[self.exhibit.pk]), {
            f"answer_{self.quiz.id}": "1",
            f"order_{self.quiz.id}": "[0, 1, 2]",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "0")
    
    def test_submit_quiz_with_no_answers(self):
        response = self.client.post(reverse("exhibits:quiz", args = [self.exhibit.pk]), {})
        self.assertEqual(response.status_code, 200) # no crash
    
    def test_score_does_not_save_for_unauthenicated_user(self):
        self.client.post(reverse("exhibits:quiz", args=[self.exhibit.pk]), {
            f"answer_{self.quiz.id}": "1",
            f"order_{self.quiz.id}": "[0, 1, 2]",
        })
        self.assertEqual(QuizScore.objects.count(), 0)
    
    def test_save_score_correct(self):
        self.client.login(username = "Alice", password = "Password1")
        self.submit_answer(0)
        score = QuizScore.objects.get(user = self.user, exhibit = self.exhibit)
        self.assertEqual(score.score_percentage, 100.0)
        self.assertEqual(score.correct_answers, 1)
    
    def test_save_score_wrong(self):
        self.client.login(username = "Alice", password = "Password1")
        self.submit_answer(1)
        score = QuizScore.objects.get(user = self.user, exhibit = self.exhibit)
        self.assertEqual(score.score_percentage, 0.0)
        self.assertEqual(score.correct_answers, 0)
    
    def test_score_updates(self):
        self.client.login(username = "Alice", password = "Password1")
        self.submit_answer(1)
        self.submit_answer(0)
        score = QuizScore.objects.get(user = self.user, exhibit = self.exhibit)
        self.assertEqual(score.score_percentage, 100.0)
        self.assertEqual(score.correct_answers, 1)
    
    def test_score_stays_the_highest(self):
        self.client.login(username = "Alice", password = "Password1")
        self.submit_answer(0)
        self.submit_answer(1)
        score = QuizScore.objects.get(user = self.user, exhibit = self.exhibit)
        self.assertEqual(score.score_percentage, 100.0)
        self.assertEqual(score.correct_answers, 1)
    
    def test_scores_are_independent_from_users(self):
        self.client.login(username = "Alice", password = "Password1")
        self.submit_answer(0)
        self.client.logout()
        user2 = create_user("Bob", "user")
        self.client.login(username = "Bob", password = "Password1")
        self.submit_answer(1)
        self.assertEqual(QuizScore.objects.get(user = self.user).score_percentage, 100.0)
        self.assertEqual(QuizScore.objects.get(user = user2).score_percentage, 0.0)