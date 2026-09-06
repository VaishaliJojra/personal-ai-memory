import unittest
from settings import MODEL_NAME


class TestSettings(unittest.TestCase):

    def test_model_name(self):
        self.assertEqual(MODEL_NAME, "qwen2.5:0.5b")


if __name__ == "__main__":
    unittest.main()
