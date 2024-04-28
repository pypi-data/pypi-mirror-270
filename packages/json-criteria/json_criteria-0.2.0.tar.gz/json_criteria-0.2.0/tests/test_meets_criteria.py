import unittest

from src.json_criteria import meets_criteria, Config

class TestMeetsCriteria(unittest.TestCase):
    def test_basic(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = { 'key': 'age', 'op': 'equal_to', 'value': 30 }
        result = meets_criteria(record, criteria)
        self.assertTrue(result)

    def test_basic2(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = { 'AND': [
            {'key': 'age', 'op': 'equal_to', 'value': 30 },
            {'key': 'name', 'op': 'equal_to', 'value': 'Joe' }
            ]
        }
        result = meets_criteria(record, criteria)
        self.assertTrue(result)

    def test_basic3(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = { 'AND': [
            {'key': 'age', 'op': 'equal_to', 'value': 30 },
            {'key': 'name', 'op': 'equal_to', 'value': 'Steve' }
            ]
        }
        result = meets_criteria(record, criteria)
        self.assertFalse(result)

    def test_custom_op_true(self):
        def custom1(record_value, value):
            return record_value + value == 100
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'custom1', 'value': 70 }
        result = meets_criteria(record, criteria, Config(custom_ops = { 'custom1': custom1 }))
        self.assertTrue(result)

    def test_custom_op_false(self):
        def custom1(record_value, value):
            return record_value + value == 100
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'custom1', 'value': 60 }
        result = meets_criteria(record, criteria, Config(custom_ops = { 'custom1': custom1 }))
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
