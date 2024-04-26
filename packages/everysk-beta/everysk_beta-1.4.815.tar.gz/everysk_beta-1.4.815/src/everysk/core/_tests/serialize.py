###############################################################################
#
# (C) Copyright 2024 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################

from unittest import TestCase
from everysk.core.datetime import Date, DateTime
from everysk.core.serialize import _default, _json_parser, dumps, loads, is_dumps_serializable

class SerializeTestCase(TestCase):

    def test_default_with_date(self):
        date_obj = Date(2024, 1, 1)
        self.assertEqual(_default(date_obj), '2024-01-01')

    def test_default_with_datetime(self):
        datetime_obj = DateTime(2024, 1, 1, 12, 0, 0)
        self.assertEqual(_default(datetime_obj), '2024-01-01T12:00:00+00:00')

    def test_default_with_undefined(self):
        self.assertEqual(_default(Undefined), Undefined.default_parse_string)

    def test_default_with_non_special_object(self):
        self.assertIsNone(_default(123))

    def test_json_parser_with_date_string(self):
        date_str = Date.today().isoformat()
        self.assertEqual(_json_parser(date_str, convert_str_to_date=False), date_str)
        self.assertIsInstance(_json_parser(date_str, convert_str_to_date=True), Date)

    def test_json_parser_with_datetime_string(self):
        datetime_str = DateTime.now().isoformat()
        self.assertEqual(_json_parser(datetime_str, convert_str_to_date=False), datetime_str)
        self.assertIsInstance(_json_parser(datetime_str, convert_str_to_date=True), DateTime)

    def test_json_parser_with_undefined(self):
        self.assertEqual(_json_parser(Undefined.default_parse_string), Undefined)

    def test_json_parser_with_dict(self):
        dict_obj = {"date": Date.today().isoformat(), "undefined": Undefined.default_parse_string}
        parsed = _json_parser(dict_obj, convert_str_to_date=True)
        self.assertIsInstance(parsed['date'], Date)
        self.assertEqual(parsed['undefined'], Undefined)

    def test_json_parser_with_list(self):
        dict_obj = [Date(2024, 1, 1).isoformat(), Undefined.default_parse_string]
        parsed = _json_parser(dict_obj, convert_str_to_date=True)
        self.assertIsInstance(parsed, list)
        self.assertListEqual(parsed, [Date(2024, 1, 1), Undefined])

    def test_dumps_and_loads_integration_with_convert_true(self):
        original_obj = {
            "date": Date.today(),
            "datetime": DateTime.now(),
            "undefined": Undefined
        }
        dumped = dumps(original_obj)
        self.assertIsInstance(dumped, bytes)
        loaded = loads(dumped.decode('utf-8'), convert_str_to_date=True)
        self.assertIsInstance(loaded['date'], Date)
        self.assertIsInstance(loaded['datetime'], DateTime)
        self.assertEqual(loaded['undefined'], Undefined)

    def test_dumps_and_loads_integration_with_convert_false(self):
        date = Date.today()
        datetime = DateTime.now()
        original_obj = {
            "date": date,
            "datetime": datetime,
            "undefined": Undefined
        }
        dumped = dumps(original_obj)
        self.assertIsInstance(dumped, bytes)
        loaded = loads(dumped.decode('utf-8'), convert_str_to_date=False)
        self.assertEqual(loaded['date'], date.isoformat())
        self.assertEqual(loaded['datetime'], datetime.isoformat())
        self.assertEqual(loaded['undefined'], Undefined)

    def test_is_dumps_serializable_basic_data_types(self):
        """ Test serialization check for basic data types """
        self.assertTrue(is_dumps_serializable(None))
        self.assertTrue(is_dumps_serializable(123))
        self.assertTrue(is_dumps_serializable(45.67))
        self.assertTrue(is_dumps_serializable("string"))
        self.assertTrue(is_dumps_serializable(True))
        self.assertTrue(is_dumps_serializable(False))
        self.assertTrue(is_dumps_serializable(Undefined))

    def test_is_dumps_serializable_date_time_objects(self):
        """ Test serialization check for date and datetime objects """
        self.assertTrue(is_dumps_serializable(Date.today()))
        self.assertTrue(is_dumps_serializable(DateTime.now()))

    def test_is_dumps_serializable_custom_object_to_dict(self):
        """ Test serialization check for custom objects with a to_dict method """
        class BaseEntity:
            def to_dict(self):
                return {"key": "value"}

        obj = BaseEntity()
        self.assertTrue(is_dumps_serializable(obj))

    def test_is_dumps_serializable_lists_and_tuples(self):
        """ Test serialization check for lists and tuples """
        self.assertTrue(is_dumps_serializable([1, "two", 3.0]))
        self.assertTrue(is_dumps_serializable((1, "two", 3.0, DateTime.now())))

    def test_is_dumps_serializable_nested_structures(self):
        """ Test serialization check for nested lists and dictionaries """
        nested_list = [1, [2, 3], ["four", 5]]
        nested_dict = {"key": ["list", {"nested_key": "nested_value"}]}
        self.assertTrue(is_dumps_serializable(nested_list))
        self.assertTrue(is_dumps_serializable(nested_dict))

    def test_is_dumps_serializable_dictionaries(self):
        """ Test serialization check for dictionaries with serializable and non-serializable keys/values """
        self.assertTrue(is_dumps_serializable({'a': 1, 'b': 2.0}))
        self.assertTrue(is_dumps_serializable({1: "one", 2: "two"}))  # Assuming keys are also checked and allowed
