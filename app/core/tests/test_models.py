from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTestCases(TestCase):
    def test_create_user_with_email_and_phonenumber_successfull(self):
        """ Test case to verify new user with email and phone number """
        email = "test@email.com"
        password = "test@1234"
        phone_number = "1234567890"
        user = get_user_model().objects.create_user(
            email=email, phone_number=phone_number, password=password
        )
        self.assertEqual(user.email, email)
        self.assertEquals(user.phone_number, phone_number)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """
        email = "test@EMAIL.com"
        password = "test@1234"
        phone_number = "1234567890"
        user = get_user_model().objects.create_user(
            email=email, phone_number=phone_number, password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_without_mandatory_fields(self):
        """ Test the invalid email / phone number for a new user raised error"""
        with self.assertRaises(ValueError):
            email = ""
            password = "test@1234"
            phone_number = "1234567890"
            user = get_user_model().objects.create_user(
                email=email, phone_number=phone_number, password=password
            )

        with self.assertRaises(ValueError):
            email = "test@EMAIL.com"
            password = "test@1234"
            phone_number = ""
            user = get_user_model().objects.create_user(
                email=email, phone_number=phone_number, password=password
            )

    def test_create_new_super_user(self):
        email = "test@EMAIL.com"
        password = "test@1234"
        phone_number = "1234567890"
        user = get_user_model().objects.create_superuser(email, phone_number, password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_admin)
