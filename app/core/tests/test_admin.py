from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        email = "admin@EMAIL.com"
        password = "admin@1234"
        phone_number = "1234567890"
        self.admin_user = get_user_model().objects.create_superuser(
            email, phone_number, password
        )

        self.client.force_login(self.admin_user)
        email = "test@EMAIL.com"
        password = "test@1234"
        phone_number = "1234567890"
        name = "Test name"
        self.user = get_user_model().objects.create_user(
            email, phone_number, password, name=name
        )

    def test_users_listed(self):
        """ Test that users created on user page """
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(
            res, self.user.name
        )  # custom django methods which reads response status
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """ Test user edit page works """
        url = reverse("admin:core_user_change", args=[self.user.id])
        # /admin/core/user/1

        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Test user create page works """
        url = reverse("admin:core_user_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
