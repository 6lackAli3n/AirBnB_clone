import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_str_method(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        base_model_dict = self.base_model.to_dict()
        self.assertTrue(isinstance(base_model_dict, dict))
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], self.base_model.id)
        self.assertEqual(base_model_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test_init_method(self):
        base_model2 = BaseModel(id="123", created_at="2023-01-01T12:00:00", updated_at="2023-01-01T12:00:00")
        self.assertEqual(base_model2.id, "123")
        self.assertEqual(base_model2.created_at, datetime.datetime(2023, 1, 1, 12, 0))
        self.assertEqual(base_model2.updated_at, datetime.datetime(2023, 1, 1, 12, 0))

    def tearDown(self):
        del self.base_model


if __name__ == '__main__':
    unittest.main()
