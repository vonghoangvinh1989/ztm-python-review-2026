import unittest
import exercise_testing


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = exercise_testing.run_guess(answer, guess)
        self.assertEqual(result, True)

    def test_input_wrong_guess(self):
        result = exercise_testing.run_guess(5, 1)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = exercise_testing.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = exercise_testing.run_guess(5, "11")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
