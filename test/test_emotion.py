import unittest
from emotion_app import analyze_emotion

class TestEmotion(unittest.TestCase):
    def test_happy(self):
        scores = analyze_emotion("I love sunshine")
        self.assertGreater(scores['joy'], 0.5)

if __name__ == '__main__':
    unittest.main()