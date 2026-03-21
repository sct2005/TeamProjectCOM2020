from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from exhibits.models import Exhibit, Bookmark, UserProfile

def create_exhibit(title, domain):
    return Exhibit.objects.create(
        title = title,
        domain=domain,
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


class BookmarksTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.exhibit1 = create_exhibit("The Snow", "Weather")
        self.exhibit2 = create_exhibit("Cosmic Microwave Background Radiation", "Energy")
        self.exhibit3 = create_exhibit("The Amazon Rainforest", "Deforestation")
        self.user = create_user("Alice", "user")
        self.client.login(username = "Alice", password = "Password1")

    def test_bookmark_created(self):
        Bookmark.objects.create(user = self.user, exhibit = self.exhibit1)
        self.assertEqual(Bookmark.objects.filter(user = self.user).count(), 1)
    
    def test_no_duplicate_bookmark(self):
        Bookmark.objects.create(user = self.user, exhibit = self.exhibit1)
        with self.assertRaises(Exception):
            Bookmark.objects.create(user = self.user, exhibit = self.exhibit1)
    
    def test_two_users_can_bookmark_same_exhibit(self):
        user2 = create_user("Bob", "user")
        Bookmark.objects.create(user = self.user, exhibit = self.exhibit1)
        Bookmark.objects.create(user = user2, exhibit = self.exhibit1)
        self.assertEqual(Bookmark.objects.filter(exhibit = self.exhibit1).count(), 2)
    
    def test_deleting_exhibit_removes_bookmark(self):
        Bookmark.objects.create(user = self.user, exhibit = self.exhibit1)
        self.exhibit1.delete()
        self.assertEqual(Bookmark.objects.filter(user = self.user).count(), 0)
    
    def test_deleting_user_removes_bookmark(self):
        Bookmark.objects.create(user = self.user, exhibit = self.exhibit1)
        self.user.delete()
        self.assertEqual(Bookmark.objects.filter(exhibit = self.exhibit1).count(), 0)
    
    def test_toggle_creates_bookmark(self):
        self.client.post(reverse("exhibits:toggle_bookmark", args = [self.exhibit1.pk]))
        self.assertTrue(Bookmark.objects.filter(user = self.user, exhibit = self.exhibit1).exists())
    
    def test_toggle_removes_bookmark(self):
        Bookmark.objects.create(user = self.user, exhibit = self.exhibit1)
        self.client.post(reverse("exhibits:toggle_bookmark", args = [self.exhibit1.pk]))
        self.assertFalse(Bookmark.objects.filter(user = self.user, exhibit = self.exhibit1).exists())
    
    def test_double_toggle(self):
        self.client.post(reverse("exhibits:toggle_bookmark", args = [self.exhibit1.pk]))
        self.client.post(reverse("exhibits:toggle_bookmark", args = [self.exhibit1.pk]))
        self.assertFalse(Bookmark.objects.filter(user = self.user, exhibit = self.exhibit1).exists())
    
    def test_toggle_with_no_user(self):
        self.client.logout()
        response = self.client.post(reverse("exhibits:toggle_bookmark", args = [self.exhibit1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Bookmark.objects.count(), 0)

    def test_bookmark_tab_shows_bookmarked_exhibits(self):
        Bookmark.objects.create(user = self.user, exhibit = self.exhibit1)
        response = self.client.get(reverse("home"), {"category": "bookmarks"})
        exhibits = response.context["exhibits"]
        titles = [exhibit.title for exhibit in exhibits]
        self.assertIn("The Snow", titles)
        self.assertNotIn("Cosmic Microwave Background Radiation", titles)
        self.assertNotIn("The Amazon Rainforest", titles)
    
    def test_no_bookmarks(self):
        response = self.client.get(reverse("home"), {"category": "bookmarks"})
        exhibits = response.context["exhibits"]
        titles = [exhibit.title for exhibit in exhibits]
        self.assertNotIn("The Snow", titles)
        self.assertNotIn("Cosmic Microwave Background Radiation", titles)
        self.assertNotIn("The Amazon Rainforest", titles)
    
    def test_no_bookmarks_tab_for_user_with_no_bookmarks(self):
        response = self.client.get(reverse("home"))
        categories = response.context["categories"]
        self.assertNotIn("bookmarks", categories)
    
    def test_bookmarks_tab_for_user_with_bookmarks(self):
        Bookmark.objects.create(user = self.user, exhibit = self.exhibit1)
        response = self.client.get(reverse("home"))
        categories = response.context["categories"]
        self.assertIn("bookmarks", categories)
    
    def test_bookmarks_not_availible_for_no_user(self):
        self.client.logout()
        response = self.client.get(reverse("home"))
        categories = response.context["categories"]
        self.assertNotIn("bookmarks", categories)

