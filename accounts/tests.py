from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class SignupPageTests(TestCase):
    """Tests for the signup page."""

    def test_url_exists_at_correct_location(self):
        """Tests that the URL for the signup view exists at the correct location."""
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        """Tests that the name for the signup view is correct."""
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        """Tests that the signup form works correctly."""
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "testpassword123",
                "password2": "testpassword123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@email.com")