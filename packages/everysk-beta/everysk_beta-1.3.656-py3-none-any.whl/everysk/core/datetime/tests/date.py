###############################################################################
#
# (C) Copyright 2023 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################

from unittest import TestCase
from everysk.core.datetime.date import date, Date
from everysk.core.datetime.datetime import datetime, DateTime

####################################################################################
#                                    Date tests                                    #
####################################################################################
class DateTestCase(TestCase):

    def test_ensure_date(self):
        ret = Date.ensure(date(2023, 1, 1))
        self.assertEqual(ret.__class__, Date)
        self.assertEqual(ret, Date(2023, 1, 1))

        ret = Date.ensure(Date(2023, 1, 1))
        self.assertEqual(ret.__class__, Date)
        self.assertEqual(ret, Date(2023, 1, 1))

    def test_ensure_datetime(self):
        ret = Date.ensure(datetime(2023, 1, 1, 12, 13, 14, 1516)) # pylint: disable=not-callable
        self.assertEqual(ret.__class__, Date)
        self.assertEqual(ret, Date(2023, 1, 1))

        ret = Date.ensure(DateTime(2023, 1, 1, 12, 13, 14, 1516))
        self.assertEqual(ret.__class__, Date)
        self.assertEqual(ret, Date(2023, 1, 1))

    def test_ensure_date_invalid(self):
        with self.assertRaisesRegex(ValueError, "Invalid instantiation of class 'Date' from 'str'"):
            Date.ensure('20210101')

    def test_date_fromisoformat(self):
        result = Date.fromisoformat('20230101')
        self.assertEqual(result.__class__, Date)
        self.assertEqual(result, Date(2023, 1, 1))

        result = Date.fromisoformat('2023-01-01')
        self.assertEqual(result.__class__, Date)
        self.assertEqual(result, Date(2023, 1, 1))

    def test_date_fromordinal(self):
        result = Date.fromordinal(1)
        self.assertEqual(result.__class__, Date)
        self.assertEqual(result, Date(1, 1, 1))

        result = Date.fromordinal(365, start_date=Date(1, 1, 1))
        self.assertEqual(result.__class__, Date)
        self.assertEqual(result, Date(1, 12, 31))

        result = Date.fromordinal(42000, start_date=Date(2020, 1, 1))
        self.assertEqual(result.__class__, Date)
        self.assertEqual(result, Date(2134, 12, 28))

    def test_date_strptime(self):
        result = Date.strptime('20230731')
        self.assertEqual(result.__class__, Date)
        self.assertEqual(result, Date(2023, 7, 31))

        result = Date.strptime('20230731', format='%Y%m%d')
        self.assertEqual(result.__class__, Date)
        self.assertEqual(result, Date(2023, 7, 31))

        result = Date.strptime('2023-07-31', format='%Y-%m-%d')
        self.assertEqual(result.__class__, Date)
        self.assertEqual(result, Date(2023, 7, 31))

    def test_date_strptime_or_null(self):
        result = Date.strptime_or_null('20230731')
        self.assertEqual(result.__class__, Date)
        self.assertEqual(result, Date(2023, 7, 31))

        result = Date.strptime_or_null('20230731', format='%Y%m%d')
        self.assertEqual(result.__class__, Date)
        self.assertEqual(result, Date(2023, 7, 31))

        result = Date.strptime_or_null('2023-07-31', format='%Y-%m-%d')
        self.assertEqual(result.__class__, Date)
        self.assertEqual(result, Date(2023, 7, 31))

        self.assertIsNone(Date.strptime_or_null('2023-07-31'))
        self.assertIsNone(Date.strptime_or_null('2023-07-31', format='%Y%m%d'))
        self.assertIsNone(Date.strptime_or_null(None))
        self.assertIsNone(Date.strptime_or_null(None, format='%Y-%m-%d'))

    def test_date_is_string_date(self):
        self.assertTrue(Date.is_string_date('20230731'))
        self.assertTrue(Date.is_string_date('20230731', format='%Y%m%d'))
        self.assertTrue(Date.is_string_date('2023-07-31', format='%Y-%m-%d'))

        self.assertFalse(Date.is_string_date('2023-07-31'))
        self.assertFalse(Date.is_string_date('2023-07-31', format='%Y%m%d'))
        self.assertFalse(Date.is_string_date(None))
        self.assertFalse(Date.is_string_date(None, format='%Y-%m-%d'))

    def test_date_strftime(self):
        self.assertEqual(Date(2023, 7, 31).strftime(), '20230731')
        self.assertEqual(Date(2023, 7, 31).strftime('%Y%m%d'), date(2023, 7, 31).strftime('%Y%m%d'))
        self.assertEqual(Date(2023, 7, 31).strftime(format='%Y%m%d'), '20230731')
        self.assertEqual(Date(2023, 7, 31).strftime(format='%Y-%m-%d'), '2023-07-31')

    def test_date_strftime_or_null(self):
        self.assertEqual(Date.strftime_or_null(Date(2023, 7, 31)), '20230731')
        self.assertEqual(Date.strftime_or_null(Date(2023, 7, 31), format='%Y%m%d'), '20230731')
        self.assertEqual(Date.strftime_or_null(Date(2023, 7, 31), format='%Y-%m-%d'), '2023-07-31')

        self.assertEqual(Date.strftime_or_null(date(2023, 7, 31)), '20230731')
        self.assertEqual(Date.strftime_or_null(date(2023, 7, 31), format='%Y%m%d'), '20230731')
        self.assertEqual(Date.strftime_or_null(date(2023, 7, 31), format='%Y-%m-%d'), '2023-07-31')

        self.assertEqual(Date.strftime_or_null(DateTime(2023, 7, 31, 12, 13, 14)), '20230731')
        self.assertEqual(Date.strftime_or_null(DateTime(2023, 7, 31, 12, 13, 14), format='%Y%m%d'), '20230731')
        self.assertEqual(Date.strftime_or_null(DateTime(2023, 7, 31, 12, 13, 14), format='%Y-%m-%d'), '2023-07-31')

        self.assertEqual(Date.strftime_or_null(datetime(2023, 7, 31, 12, 13, 14)), '20230731') # pylint: disable=not-callable
        self.assertEqual(Date.strftime_or_null(datetime(2023, 7, 31, 12, 13, 14), format='%Y%m%d'), '20230731') # pylint: disable=not-callable
        self.assertEqual(Date.strftime_or_null(datetime(2023, 7, 31, 12, 13, 14), format='%Y-%m-%d'), '2023-07-31') # pylint: disable=not-callable

        self.assertIsNone(Date.strftime_or_null('2023-07-31'))
        self.assertIsNone(Date.strftime_or_null('2023-07-31', format='%Y%m%d'))
        self.assertIsNone(Date.strftime_or_null(None))
        self.assertIsNone(Date.strftime_or_null(None, format='%Y-%m-%d'))

    def test_date_is_date(self):
        self.assertTrue(Date.is_date(date(2023, 7, 31)))
        self.assertTrue(Date.is_date(Date(2023, 7, 31)))

        self.assertFalse(Date.is_date(DateTime(2023, 7, 31)))
        self.assertFalse(Date.is_date(DateTime(2023, 7, 31)))
        self.assertFalse(Date.is_date(None))

    def test_date_today(self):
        result = Date.today()
        self.assertEqual(result.__class__, Date)
        self.assertEqual(result, date.today())

    def test_date_is_today(self):
        self.assertTrue(Date.is_today(Date.today()))
        self.assertFalse(Date.is_today(Date(2023, 1, 1)))

    def test_is_date(self):
        self.assertTrue(Date.is_date(Date.today()))
        self.assertTrue(Date.is_date(Date(2023, 1, 1)))
        self.assertTrue(Date.is_date(date(2023, 1, 1)))
        self.assertFalse(Date.is_date(DateTime.now()))
        self.assertFalse(Date.is_date('date'))
        self.assertFalse(Date.is_date(2022))

    def test_date_quarter(self):
        self.assertEqual(Date(2023, 1, 1).quarter, 1)
        self.assertEqual(Date(2023, 3, 31).quarter, 1)
        self.assertEqual(Date(2023, 4, 1).quarter, 2)
        self.assertEqual(Date(2023, 6, 30).quarter, 2)
        self.assertEqual(Date(2023, 7, 1).quarter, 3)
        self.assertEqual(Date(2023, 9, 30).quarter, 3)
        self.assertEqual(Date(2023, 10, 1).quarter, 4)
        self.assertEqual(Date(2023, 12, 31).quarter, 4)

    def test_date_month_name(self):
        self.assertEqual(Date(2023, 1, 1).month_name, 'January')
        self.assertEqual(Date(2023, 2, 1).month_name, 'February')
        self.assertEqual(Date(2023, 3, 1).month_name, 'March')
        self.assertEqual(Date(2023, 4, 1).month_name, 'April')
        self.assertEqual(Date(2023, 5, 1).month_name, 'May')
        self.assertEqual(Date(2023, 6, 1).month_name, 'June')
        self.assertEqual(Date(2023, 7, 1).month_name, 'July')
        self.assertEqual(Date(2023, 8, 1).month_name, 'August')
        self.assertEqual(Date(2023, 9, 1).month_name, 'September')
        self.assertEqual(Date(2023, 10, 1).month_name, 'October')
        self.assertEqual(Date(2023, 11, 1).month_name, 'November')
        self.assertEqual(Date(2023, 12, 1).month_name, 'December')

    def test_date_week_of_year(self):
        self.assertEqual(Date(2023, 1, 1).week_of_year, 1)
        self.assertEqual(Date(2023, 6, 30).week_of_year, 26)
        self.assertEqual(Date(2023, 9, 30).week_of_year, 39)
        self.assertEqual(Date(2023, 12, 31).week_of_year, 53)

    def test_date_week_of_month(self):
        self.assertEqual(Date(2023, 1, 1).week_of_month, 1)
        self.assertEqual(Date(2023, 6, 8).week_of_month, 2)
        self.assertEqual(Date(2023, 9, 15).week_of_month, 3)
        self.assertEqual(Date(2023, 12, 31).week_of_month, 5)

    def test_date_day_name(self):
        self.assertEqual(Date(2023, 1, 1).day_name, 'Sunday')
        self.assertEqual(Date(2023, 1, 2).day_name, 'Monday')
        self.assertEqual(Date(2023, 1, 3).day_name, 'Tuesday')
        self.assertEqual(Date(2023, 1, 4).day_name, 'Wednesday')
        self.assertEqual(Date(2023, 1, 5).day_name, 'Thursday')
        self.assertEqual(Date(2023, 1, 6).day_name, 'Friday')
        self.assertEqual(Date(2023, 1, 7).day_name, 'Saturday')

    def test_date_day_of_year(self):
        self.assertEqual(Date(2023, 1, 1).day_of_year, 1)
        self.assertEqual(Date(2023, 6, 30).day_of_year, 181)
        self.assertEqual(Date(2023, 9, 30).day_of_year, 273)
        self.assertEqual(Date(2023, 12, 31).day_of_year, 365)

    def test_date_toordinal(self):
        self.assertEqual(Date(1, 1, 1).toordinal(), 1)
        self.assertEqual(Date(1, 12, 31).toordinal(start_date=Date(1, 1, 1)), 365)
        self.assertEqual(Date(2134, 12, 28).toordinal(start_date=Date(2020, 1, 1)), 42000)

    def test_date_get_last_day_of_week(self):
        ret = Date(2023, 1, 1).get_last_day_of_week()
        self.assertEqual(ret, Date(2023, 1, 7))
        self.assertEqual(ret.__class__, Date)
        self.assertEqual(Date(2023, 1, 7).get_last_day_of_week(), Date(2023, 1, 7))
        self.assertEqual(Date(2023, 1, 7).get_last_day_of_week(bizdays=True), Date(2023, 1, 6))
        self.assertEqual(Date(2023, 1, 1).get_last_day_of_week(bizdays=True, calendar='ANBIMA'), Date(2023, 1, 6))
        self.assertEqual(Date(2023, 4, 3).get_last_day_of_week(), Date(2023, 4, 8))
        self.assertEqual(Date(2023, 4, 3).get_last_day_of_week(bizdays=True), Date(2023, 4, 7))
        self.assertEqual(Date(2023, 4, 3).get_last_day_of_week(bizdays=True, calendar='ANBIMA'), Date(2023, 4, 6))

    def test_date_get_last_day_of_month(self):
        self.assertEqual(Date(2018, 5, 15).get_last_day_of_month().__class__, Date)
        self.assertEqual(Date(2018, 5, 15).get_last_day_of_month(), Date(2018, 5, 31))
        self.assertEqual(Date(2018, 5, 15).get_last_day_of_month(bizdays=True), Date(2018, 5, 31))
        self.assertEqual(Date(2018, 5, 15).get_last_day_of_month(bizdays=True, calendar='ANBIMA'), Date(2018, 5, 30))

    def test_date_get_last_day_of_quarter(self):
        self.assertEqual(Date(2023, 1, 15).get_last_day_of_quarter().__class__, Date)
        self.assertEqual(Date(2023, 1, 15).get_last_day_of_quarter(), Date(2023, 3, 31))
        self.assertEqual(Date(2023, 4, 15).get_last_day_of_quarter(), Date(2023, 6, 30))
        self.assertEqual(Date(2023, 7, 15).get_last_day_of_quarter(bizdays=True), Date(2023, 9, 29))
        self.assertEqual(Date(2023, 11, 15).get_last_day_of_quarter(bizdays=True, calendar='ANBIMA'), Date(2023, 12, 29))

    def test_date_get_last_day_of_year(self):
        self.assertEqual(Date(2023, 1, 15).get_last_day_of_year().__class__, Date)
        self.assertEqual(Date(2023, 1, 15).get_last_day_of_year(), Date(2023, 12, 31))
        self.assertEqual(Date(2023, 7, 15).get_last_day_of_year(bizdays=True), Date(2023, 12, 29))
        self.assertEqual(Date(2023, 11, 15).get_last_day_of_year(bizdays=True, calendar='ANBIMA'), Date(2023, 12, 29))

    def test_date_is_last_day_of_week(self):
        self.assertTrue(Date(2023, 4, 8).is_last_day_of_week())
        self.assertFalse(Date(2023, 4, 7).is_last_day_of_week())
        self.assertFalse(Date(2023, 4, 6).is_last_day_of_week())
        self.assertFalse(Date(2023, 4, 8).is_last_day_of_week(bizdays=True))
        self.assertTrue(Date(2023, 4, 7).is_last_day_of_week(bizdays=True))
        self.assertTrue(Date(2023, 4, 6).is_last_day_of_week(bizdays=True, calendar='ANBIMA'))

    def test_date_is_last_day_of_month(self):
        self.assertTrue(Date(2023, 1, 31).is_last_day_of_month())
        self.assertFalse(Date(2023, 2, 27).is_last_day_of_month())
        self.assertTrue(Date(2023, 12, 31).is_last_day_of_month())
        self.assertTrue(Date(2023, 4, 28).is_last_day_of_month(bizdays=True))
        self.assertFalse(Date(2023, 4, 30).is_last_day_of_month(bizdays=True))
        self.assertFalse(Date(2023, 12, 31).is_last_day_of_month(bizdays=True, calendar='ANBIMA'))

    def test_date_is_last_day_of_quarter(self):
        self.assertFalse(Date(2023, 1, 1).is_last_day_of_quarter())
        self.assertTrue(Date(2023, 3, 31).is_last_day_of_quarter())
        self.assertFalse(Date(2023, 4, 1).is_last_day_of_quarter())
        self.assertTrue(Date(2023, 6, 30).is_last_day_of_quarter())
        self.assertFalse(Date(2023, 7, 1).is_last_day_of_quarter())
        self.assertTrue(Date(2023, 9, 30).is_last_day_of_quarter())
        self.assertFalse(Date(2023, 10, 1).is_last_day_of_quarter())
        self.assertTrue(Date(2023, 12, 31).is_last_day_of_quarter())
        self.assertTrue(Date(2023, 12, 29).is_last_day_of_quarter(bizdays=True))
        self.assertTrue(Date(2023, 12, 29).is_last_day_of_quarter(bizdays=True, calendar='ANBIMA'))
        self.assertFalse(Date(2023, 12, 31).is_last_day_of_quarter(bizdays=True))
        self.assertFalse(Date(2023, 12, 31).is_last_day_of_quarter(bizdays=True, calendar='ANBIMA'))

    def test_date_is_last_day_of_year(self):
        self.assertFalse(Date(2023, 1, 1).is_last_day_of_year())
        self.assertFalse(Date(2023, 1, 31).is_last_day_of_year())
        self.assertTrue(Date(2023, 12, 31).is_last_day_of_year())
        self.assertTrue(Date(2023, 12, 29).is_last_day_of_year(bizdays=True))
        self.assertTrue(Date(2023, 12, 29).is_last_day_of_year(bizdays=True, calendar='ANBIMA'))
        self.assertFalse(Date(2023, 12, 30).is_last_day_of_year(bizdays=True))
        self.assertFalse(Date(2023, 12, 31).is_last_day_of_year(bizdays=True, calendar='ANBIMA'))

    def test_date_get_first_day_of_week(self):
        self.assertEqual(Date(2023, 1, 1).get_first_day_of_week().__class__, Date)
        self.assertEqual(Date(2023, 1, 1).get_first_day_of_week(), Date(2023, 1, 1))
        self.assertEqual(Date(2023, 1, 5).get_first_day_of_week(), Date(2023, 1, 1))
        self.assertEqual(Date(2023, 1, 7).get_first_day_of_week(bizdays=True), Date(2023, 1, 2))
        self.assertEqual(Date(2023, 1, 1).get_first_day_of_week(bizdays=True, calendar='ANBIMA'), Date(2023, 1, 2))
        self.assertEqual(Date(2023, 4, 3).get_first_day_of_week(), Date(2023, 4, 2))
        self.assertEqual(Date(2023, 4, 3).get_first_day_of_week(bizdays=True), Date(2023, 4, 3))
        self.assertEqual(Date(2023, 4, 3).get_first_day_of_week(bizdays=True, calendar='ANBIMA'), Date(2023, 4, 3))
        self.assertEqual(Date(2023, 5, 4).get_first_day_of_week(bizdays=True, calendar='ANBIMA'), Date(2023, 5, 2))

    def test_date_get_first_day_of_month(self):
        self.assertEqual(Date(2023, 5, 15).get_first_day_of_month().__class__, Date)
        self.assertEqual(Date(2023, 5, 15).get_first_day_of_month(), Date(2023, 5, 1))
        self.assertEqual(Date(2023, 1, 15).get_first_day_of_month(bizdays=True), Date(2023, 1, 2))
        self.assertEqual(Date(2023, 5, 15).get_first_day_of_month(bizdays=True, calendar='ANBIMA'), Date(2023, 5, 2))

    def test_date_is_first_day_of_week(self):
        self.assertTrue(Date(2023, 1, 1).is_first_day_of_week())
        self.assertTrue(Date(2023, 4, 2).is_first_day_of_week())
        self.assertFalse(Date(2023, 1, 1).is_first_day_of_week(bizdays=True))
        self.assertTrue(Date(2018, 1, 2).is_first_day_of_week(bizdays=True, calendar='ANBIMA'))

    def test_date_get_first_day_of_quarter(self):
        self.assertEqual(Date(2023, 1, 15).get_first_day_of_quarter().__class__, Date)
        self.assertEqual(Date(2023, 1, 15).get_first_day_of_quarter(), Date(2023, 1, 1))
        self.assertEqual(Date(2023, 4, 15).get_first_day_of_quarter(), Date(2023, 4, 1))
        self.assertEqual(Date(2023, 4, 15).get_first_day_of_quarter(bizdays=True), Date(2023, 4, 3))
        self.assertEqual(Date(2023, 11, 15).get_first_day_of_quarter(bizdays=True, calendar='ANBIMA'), Date(2023, 10, 2))

    def test_date_get_first_day_of_year(self):
        self.assertEqual(Date(2023, 1, 15).get_first_day_of_year().__class__, Date)
        self.assertEqual(Date(2023, 1, 15).get_first_day_of_year(), Date(2023, 1, 1))
        self.assertEqual(Date(2023, 7, 15).get_first_day_of_year(bizdays=True), Date(2023, 1, 2))
        self.assertEqual(Date(2018, 11, 15).get_first_day_of_year(bizdays=True, calendar='ANBIMA'), Date(2018, 1, 2))

    def test_date_is_first_day_of_month(self):
        self.assertTrue(Date(2023, 1, 1).is_first_day_of_month())
        self.assertTrue(Date(2023, 12, 1).is_first_day_of_month())
        self.assertFalse(Date(2023, 12, 31).is_first_day_of_month())
        self.assertTrue(Date(2023, 1, 2).is_first_day_of_month(bizdays=True))
        self.assertFalse(Date(2023, 1, 1).is_first_day_of_month(bizdays=True))
        self.assertTrue(Date(2018, 1, 2).is_first_day_of_month(bizdays=True, calendar='ANBIMA'))
        self.assertFalse(Date(2018, 1, 1).is_first_day_of_month(bizdays=True, calendar='ANBIMA'))

    def test_date_is_first_day_of_quarter(self):
        self.assertTrue(Date(2023, 1, 1).is_first_day_of_quarter())
        self.assertFalse(Date(2023, 3, 31).is_first_day_of_quarter())
        self.assertTrue(Date(2023, 4, 1).is_first_day_of_quarter())
        self.assertFalse(Date(2023, 6, 30).is_first_day_of_quarter())
        self.assertTrue(Date(2023, 7, 1).is_first_day_of_quarter())
        self.assertFalse(Date(2023, 9, 30).is_first_day_of_quarter())
        self.assertTrue(Date(2023, 10, 1).is_first_day_of_quarter())
        self.assertFalse(Date(2023, 12, 31).is_first_day_of_quarter())
        self.assertTrue(Date(2023, 1, 2).is_first_day_of_quarter(bizdays=True))
        self.assertTrue(Date(2018, 7, 2).is_first_day_of_quarter(bizdays=True))
        self.assertTrue(Date(2018, 1, 2).is_first_day_of_quarter(bizdays=True, calendar='ANBIMA'))

    def test_date_is_first_day_of_year(self):
        self.assertTrue(Date(2023, 1, 1).is_first_day_of_year())
        self.assertTrue(Date(2023, 1, 2).is_first_day_of_year(bizdays=True))
        self.assertTrue(Date(2018, 1, 2).is_first_day_of_year(bizdays=True, calendar='ANBIMA'))
        self.assertFalse(Date(2023, 12, 30).is_first_day_of_year(bizdays=True))
        self.assertFalse(Date(2023, 12, 31).is_first_day_of_year(bizdays=True, calendar='ANBIMA'))

    def test_date_delta(self):
        self.assertEqual(Date(2023, 7, 31).delta(period=5, periodicity='D').__class__, Date)
        self.assertEqual(Date(2023, 7, 31).delta(period=5, periodicity='D'), Date(2023, 8, 5))
        self.assertEqual(Date(2023, 7, 31).delta(period=2, periodicity='W'), Date(2023, 8, 14))
        self.assertEqual(Date(2023, 7, 31).delta(period=1, periodicity='M'), Date(2023, 8, 31))
        self.assertEqual(Date(2023, 7, 31).delta(period=2, periodicity='Y'), Date(2025, 7, 31))
        self.assertEqual(Date(2023, 4, 30).delta(period=1, periodicity='B', calendar='ANBIMA'), Date(2023, 5, 2))

        with self.assertRaisesRegex(ValueError, "Invalid periodicity. Please choose one of the following: D, B, W, M, Y."):
            self.assertEqual(Date(2023, 7, 31).delta(period=5, periodicity='INVALID'), Date(2023, 8, 5))

    def test_date_days_delta(self):
        self.assertEqual(Date(2023, 7, 31).days_delta(5).__class__, Date)
        self.assertEqual(Date(2023, 7, 31).days_delta(5), Date(2023, 8, 5))
        self.assertEqual(Date(2023, 7, 31).days_delta(-5), Date(2023, 7, 26))

    def test_date_bizdays_delta(self):
        self.assertEqual(Date(2023, 7, 31).bizdays_delta(5).__class__, Date)
        self.assertEqual(Date(2023, 7, 31).bizdays_delta(5), Date(2023, 8, 7))
        self.assertEqual(Date(2023, 7, 31).bizdays_delta(-5), Date(2023, 7, 24))
        self.assertEqual(Date(2023, 4, 30).bizdays_delta(1, calendar='ANBIMA'), Date(2023, 5, 2))

        with self.assertRaisesRegex(ValueError, "Value out of range"):
            self.assertEqual(Date(2023, 7, 31).bizdays_delta(50001), Date(2023, 8, 5))

    def test_date_weeks_delta(self):
        self.assertEqual(Date(2023, 7, 31).weeks_delta(5).__class__, Date)
        self.assertEqual(Date(2023, 7, 31).weeks_delta(5), Date(2023, 9, 4))
        self.assertEqual(Date(2023, 7, 31).weeks_delta(-5), Date(2023, 6, 26))

    def test_date_months_delta(self):
        self.assertEqual(Date(2023, 7, 31).months_delta(5).__class__, Date)
        self.assertEqual(Date(2023, 7, 31).months_delta(5), Date(2023, 12, 31))
        self.assertEqual(Date(2023, 7, 31).months_delta(-5), Date(2023, 2, 28))

    def test_date_months_delta_with_leap_year(self):
        self.assertEqual(Date(2020, 3, 31).months_delta(1), Date(2020, 4, 30))
        self.assertEqual(Date(2020, 2, 29).months_delta(1), Date(2020, 3, 29))
        self.assertEqual(Date(2020, 3, 31).months_delta(-1), Date(2020, 2, 29))
        self.assertEqual(Date(2020, 2, 29).months_delta(12), Date(2021, 2, 28))
        self.assertEqual(Date(2020, 2, 29).months_delta(-12), Date(2019, 2, 28))

    def test_date_years_delta(self):
        self.assertEqual(Date(2023, 7, 31).years_delta(5).__class__, Date)
        self.assertEqual(Date(2023, 7, 31).years_delta(5), Date(2028, 7, 31))
        self.assertEqual(Date(2023, 7, 31).years_delta(-5), Date(2018, 7, 31))

    def test_date_years_delta_with_leap_year(self):
        self.assertEqual(Date(2020, 2, 29).years_delta(1), Date(2021, 2, 28))
        self.assertEqual(Date(2020, 2, 29).years_delta(-1), Date(2019, 2, 28))
        self.assertEqual(Date(2020, 2, 29).years_delta(4), Date(2024, 2, 29))
        self.assertEqual(Date(2020, 2, 29).years_delta(-4), Date(2016, 2, 29))

    def test_date_diff(self):
        self.assertEqual(Date.diff(start_date=Date(2023, 7, 31), end_date=Date(2023, 7, 31), periodicity='D'), 0)
        self.assertEqual(Date.diff(start_date=Date(2023, 7, 31), end_date=Date(2023, 8, 5), periodicity='D'), 5)
        self.assertEqual(Date.diff(start_date=Date(2023, 7, 31), end_date=Date(2023, 8, 14), periodicity='W'), 2)
        self.assertEqual(Date.diff(start_date=Date(2023, 7, 31), end_date=Date(2023, 8, 31), periodicity='M'), 1)
        self.assertEqual(Date.diff(start_date=Date(2023, 7, 31), end_date=Date(2025, 7, 31), periodicity='Y'), 2)
        self.assertEqual(Date.diff(start_date=Date(2023, 4, 30), end_date=Date(2023, 5, 2), periodicity='B', calendar='ANBIMA'), 1)
        self.assertEqual(Date.diff(start_date=date(2023, 4, 30), end_date=date(2023, 5, 2), periodicity='B', calendar='ANBIMA'), 1)

        with self.assertRaisesRegex(ValueError, "Invalid periodicity. Please choose one of the following: D, B, W, M, Y."):
            self.assertEqual(Date.diff(start_date=Date(2023, 7, 31), end_date=Date(2023, 8, 5), periodicity='INVALID'), 5)

    def test_date_days_diff(self):
        self.assertEqual(Date.days_diff(start_date=Date(2023, 8, 5), end_date=Date(2023, 7, 31)), -5)
        self.assertEqual(Date.days_diff(start_date=Date(2023, 7, 31), end_date=Date(2023, 8, 5)), 5)
        self.assertEqual(Date.days_diff(start_date=date(2023, 7, 31), end_date=date(2023, 8, 5)), 5)
        self.assertEqual(Date.days_diff(start_date=Date(2024, 2, 19), end_date=Date(2024, 2, 20)), 1)
        self.assertEqual(Date.days_diff(start_date=Date(2023, 5, 2), end_date=Date(2023, 4, 30)), -2)

    def test_date_bizdays_diff(self):
        self.assertEqual(Date.bizdays_diff(start_date=Date(2023, 8, 7), end_date=Date(2023, 7, 31)), -5)
        self.assertEqual(Date.bizdays_diff(start_date=Date(2023, 7, 31), end_date=Date(2023, 8, 7)), 5)
        self.assertEqual(Date.bizdays_diff(start_date=Date(2023, 5, 2), end_date=Date(2023, 4, 30), calendar='ANBIMA'), -1)
        self.assertEqual(Date.bizdays_diff(start_date=date(2023, 5, 2), end_date=date(2023, 4, 30), calendar='ANBIMA'), -1)
        self.assertEqual(Date.bizdays_diff(start_date=Date(2024, 2, 19), end_date=Date(2024, 2, 20), calendar='ANBIMA'), 1)
        self.assertEqual(Date.bizdays_diff(start_date=Date(2023, 5, 2), end_date=Date(2023, 4, 30), calendar='ANBIMA'), -1)

    def test_date_weeks_diff(self):
        self.assertEqual(Date.weeks_diff(start_date=Date(2023, 9, 4), end_date=Date(2023, 7, 31)), -5)
        self.assertEqual(Date.weeks_diff(start_date=Date(2023, 7, 31), end_date=Date(2023, 9, 4)), 5)
        self.assertEqual(Date.weeks_diff(start_date=date(2023, 7, 31), end_date=date(2023, 9, 4)), 5)

    def test_date_months_diff(self):
        self.assertEqual(Date.months_diff(start_date=Date(2023, 12, 31), end_date=Date(2023, 7, 31)), -5)
        self.assertEqual(Date.months_diff(start_date=Date(2023, 7, 31), end_date=Date(2023, 12, 31)), 5)
        self.assertEqual(Date.months_diff(start_date=Date(2023, 7, 31), end_date=Date(2023, 12, 29)), 4)
        self.assertEqual(Date.months_diff(start_date=date(2023, 7, 31), end_date=date(2023, 12, 29)), 4)

    def test_date_years_diff(self):
        self.assertEqual(Date.years_diff(start_date=Date(2028, 7, 31), end_date=Date(2023, 7, 31)), -5)
        self.assertEqual(Date.years_diff(start_date=Date(2023, 7, 31), end_date=Date(2028, 7, 31)), 5)
        self.assertEqual(Date.years_diff(start_date=Date(2023, 7, 31), end_date=Date(2028, 7, 29)), 4)
        self.assertEqual(Date.years_diff(start_date=date(2023, 7, 31), end_date=date(2028, 7, 29)), 4)

    def test_date_range(self):
        self.assertEqual(Date.range(Date(2023, 1, 1), Date(2023, 1, 1)), [])
        self.assertListEqual(
            Date.range(Date(2021, 12, 23), Date(2022, 1, 2)),
            [
                Date(2021, 12, 23),
                Date(2021, 12, 24),
                Date(2021, 12, 25),
                Date(2021, 12, 26),
                Date(2021, 12, 27),
                Date(2021, 12, 28),
                Date(2021, 12, 29),
                Date(2021, 12, 30),
                Date(2021, 12, 31),
                Date(2022, 1, 1)
            ]
        )

        self.assertEqual(
            Date.range(date(2021, 12, 23), date(2022, 1, 2)),
            [
                Date(2021, 12, 23),
                Date(2021, 12, 24),
                Date(2021, 12, 25),
                Date(2021, 12, 26),
                Date(2021, 12, 27),
                Date(2021, 12, 28),
                Date(2021, 12, 29),
                Date(2021, 12, 30),
                Date(2021, 12, 31),
                Date(2022, 1, 1)
            ]
        )

        self.assertEqual(
            Date.range(Date(2023, 4, 18), Date(2023, 5, 3), periodicity='B', calendar='ANBIMA'),
            [
                Date(2023, 4, 18),
                Date(2023, 4, 19),
                Date(2023, 4, 20),
                Date(2023, 4, 24),
                Date(2023, 4, 25),
                Date(2023, 4, 26),
                Date(2023, 4, 27),
                Date(2023, 4, 28),
                Date(2023, 5, 2)]
        )

    def test_date_range_invalid_periodicity(self):
        with self.assertRaisesRegex(ValueError, 'Invalid periodicity. Please choose one of the following: D, B.'):
            Date.range(Date(2021, 12, 23), Date(2022, 1, 2), periodicity='invalid')

    def test_date_range_out_of_range_date(self):
        with self.assertRaisesRegex(ValueError, 'Value out of range'):
            Date.range(Date(2000, 1, 1), Date(2300, 1, 1))

    def test_date_range_return_correct_type(self):
        start_date, end_date = Date.date_range('custom_range', '', '', None, Date(2023, 9, 28))
        self.assertEqual(start_date.__class__, Date)
        self.assertEqual(end_date.__class__, Date)
        self.assertEqual(start_date, Date(2008, 1, 1))
        self.assertEqual(end_date, Date(2023, 9, 28))

    def test_date_days_range(self):
        self.assertEqual(Date.days_range(Date(2023, 1, 1), Date(2023, 1, 1)), [])
        self.assertListEqual(
            Date.days_range(Date(2021, 12, 23), Date(2022, 1, 2)),
            [
                Date(2021, 12, 23),
                Date(2021, 12, 24),
                Date(2021, 12, 25),
                Date(2021, 12, 26),
                Date(2021, 12, 27),
                Date(2021, 12, 28),
                Date(2021, 12, 29),
                Date(2021, 12, 30),
                Date(2021, 12, 31),
                Date(2022, 1, 1)
            ]
        )

        self.assertListEqual(
            Date.days_range(date(2021, 12, 23), date(2022, 1, 2)),
            [
                Date(2021, 12, 23),
                Date(2021, 12, 24),
                Date(2021, 12, 25),
                Date(2021, 12, 26),
                Date(2021, 12, 27),
                Date(2021, 12, 28),
                Date(2021, 12, 29),
                Date(2021, 12, 30),
                Date(2021, 12, 31),
                Date(2022, 1, 1)
            ]
        )

    def test_date_bizdays_range_with_calendar(self):
        self.assertListEqual(
            Date.bizdays_range(Date(2023, 4, 18), Date(2023, 5, 3), calendar='ANBIMA'),
            [
                Date(2023, 4, 18),
                Date(2023, 4, 19),
                Date(2023, 4, 20),
                Date(2023, 4, 24),
                Date(2023, 4, 25),
                Date(2023, 4, 26),
                Date(2023, 4, 27),
                Date(2023, 4, 28),
                Date(2023, 5, 2)]
        )

        self.assertListEqual(
            Date.bizdays_range(date(2023, 4, 18), date(2023, 5, 3), calendar='ANBIMA'),
            [
                Date(2023, 4, 18),
                Date(2023, 4, 19),
                Date(2023, 4, 20),
                Date(2023, 4, 24),
                Date(2023, 4, 25),
                Date(2023, 4, 26),
                Date(2023, 4, 27),
                Date(2023, 4, 28),
                Date(2023, 5, 2)]
        )

    def test_date_bizdays_range_without_calendar(self):
        self.assertEqual(
            Date.bizdays_range(Date(2023, 4, 18), Date(2023, 5, 3)),
            [
                Date(2023, 4, 18),
                Date(2023, 4, 19),
                Date(2023, 4, 20),
                Date(2023, 4, 21),
                Date(2023, 4, 24),
                Date(2023, 4, 25),
                Date(2023, 4, 26),
                Date(2023, 4, 27),
                Date(2023, 4, 28),
                Date(2023, 5, 1),
                Date(2023, 5, 2)]
        )

    def get_date_parameters(self, range_type='single_date', period='days', nPeriod='10', start_date=Date(2023, 5, 1), end_date=Date(2023, 5, 25)):
        return range_type, period, nPeriod, start_date, end_date

    def test_date_range_single_date(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters()
        cmp = (Date(2023, 5, 25), Date(2023, 5, 25))
        res = Date.date_range(range_type, period, nPeriod, start_date, end_date)
        self.assertEqual(res, cmp)

    def test_date_range_single_date_without_end_date(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(end_date='')
        today = date.today()
        cmp = (today, today)
        res = Date.date_range(range_type, period, nPeriod, start_date, end_date)
        self.assertEqual(res, cmp)

    def test_date_range_custom_range(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='custom_range')
        res = Date.date_range(range_type, period, nPeriod, start_date, end_date)
        cmp = (Date(2023, 5, 1), Date(2023, 5, 25))
        self.assertEqual(res, cmp)

    def test_date_range_custom_range_without_start_date(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='custom_range', start_date='')
        cmp = (Date(2008, 1, 1), Date(2023, 5, 25))
        res = Date.date_range(range_type, period, nPeriod, start_date, end_date)
        self.assertEqual(res, cmp)

    def test_date_range_n_period_days(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='n_period')
        cmp = (Date(2023, 5, 15), Date(2023, 5, 25))
        res = Date.date_range(range_type, period, nPeriod, start_date, end_date)
        self.assertEqual(res, cmp)

    def test_date_range_n_period_weeks(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='n_period', period='weeks')
        cmp = (Date(2023, 3, 16), Date(2023, 5, 25))
        res = Date.date_range(range_type, period, nPeriod, start_date, end_date)
        self.assertEqual(res, cmp)

    def test_date_range_n_period_months(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='n_period', period='months')
        cmp = (Date(2022, 7, 25), Date(2023, 5, 25))
        res = Date.date_range(range_type, period, nPeriod, start_date, end_date)
        self.assertEqual(res, cmp)

    def test_date_range_n_period_years(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='n_period', period='years')
        cmp = (Date(2013, 5, 25), Date(2023, 5, 25))
        res = Date.date_range(range_type, period, nPeriod, start_date, end_date)
        self.assertEqual(res, cmp)

    def test_date_range_invalid_n_period(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='n_period', period='invalid')
        error_message = 'invalid n period'
        with self.assertRaises(Exception) as error:
            Date.date_range(range_type, period, nPeriod, start_date, end_date)
        self.assertTrue(error_message in str(error.exception))

    def test_date_range_period_to_date_mtd(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='period_to_date', period='mtd')
        cmp = (Date(2023, 5, 1), Date(2023, 5, 25))
        res = Date.date_range(range_type, period, nPeriod, start_date, end_date)
        self.assertEqual(res, cmp)

    def test_date_range_period_to_date_qtd(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='period_to_date', period='qtd')
        cmp = (Date(2023, 4, 1), Date(2023, 5, 25))
        res = Date.date_range(range_type, period, nPeriod, start_date, end_date)
        self.assertEqual(res, cmp)

    def test_date_range_period_to_date_ytd(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='period_to_date', period='ytd')
        cmp = (Date(2023, 1, 1), Date(2023, 5, 25))
        res = Date.date_range(range_type, period, nPeriod, start_date, end_date)
        self.assertEqual(res, cmp)

    def test_date_range_end_period_to_date_ytd(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='end_period_to_date', period='ytd')
        cmp = (Date(2022, 12, 30), Date(2023, 5, 25))
        res = Date.date_range(range_type, period, nPeriod, start_date, end_date)
        self.assertEqual(res, cmp)

    def test_date_range_period_to_date_invalid_period(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='end_period_to_date', period='invalid')
        with self.assertRaisesRegex(ValueError, "invalid period to date"):
            Date.date_range(range_type, period, nPeriod, start_date, end_date)

    def test_date_range_invalid_range_type(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='invalid')
        with self.assertRaisesRegex(ValueError, "invalid range type"):
            Date.date_range(range_type, period, nPeriod, start_date, end_date)

    def test_date_range_invalid_end_date(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='period_to_date', period='mtd', end_date='20230101')
        with self.assertRaisesRegex(ValueError, 'Invalid end_date type'):
            Date.date_range(range_type, period, nPeriod, start_date, end_date)

    def test_date_range_invalid_start_date(self):
        range_type, period, nPeriod, start_date, end_date = self.get_date_parameters(range_type='period_to_date', period='mtd', start_date='20230101')
        with self.assertRaisesRegex(ValueError, 'Invalid start_date type'):
            Date.date_range(range_type, period, nPeriod, start_date, end_date)
