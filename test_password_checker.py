import unittest
from password_checker import check_password

class TestPasswordChecker(unittest.TestCase):

    def test_common_password(self):
        score, rating, feedback = check_password("password123")
        self.assertIn("Warning: this is a commonly used password.", feedback)

    def test_high_score(self):
        score, rating, feedback = check_password("BlueTiger!River82")
        self.assertEqual(score, 5)
        self.assertEqual(rating, "High")

    def test_repeated_characters(self):
        score, rating, feedback = check_password("AAAAAAAAAAAAAA!1")
        self.assertIn("Warning: A character is repeated 5 or more times!", feedback)

if __name__ == "__main__":
            unittest.main()