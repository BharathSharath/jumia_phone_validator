import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_validate_phone_number(self):
        payload = {'phone_number': '+123456789'}
        response = self.app.post('/validate', json=payload)
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('phone_number', data)
        self.assertIn('is_valid', data)

if __name__ == '__main__':
    unittest.main()
