###############################################################################
#
# (C) Copyright 2023 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
# pylint: disable=unused-import

## Remember to prefix all import with EveryskLib to avoid clash with other tests

## Cloud function Test Cases
try:
    from everysk.core.cloud_function.tests import CloudFunctionTestCase as EveryskLibCloudFunctionTestCase
except ModuleNotFoundError as error:
    # This will prevent running these tests if redis is not installed
    if not error.args[0].startswith("No module named 'redis'"):
        raise error

## Compress Test Cases
from everysk.core._tests.compress import (
    CompressJsonTestCase as EveryskLibCompressJsonTestCase,
    CompressPickleTestCase as EveryskLibCompressPickleTestCase
)

## Config Test Cases
from everysk.core._tests.config import SettingsModulesTestCase as EveryskLibSettingsModulesTestCase, SettingsTestCase as EveryskLibSettingsTestCase

## Date, DateTime Test Cases
from everysk.core.datetime.tests.date import DateTestCase as EveryskLibDateTestCase
from everysk.core.datetime.tests.datetime import DateTimeTestCase as EveryskLibDateTimeTestCase
from everysk.core.datetime.tests.date_mixin import GetHolidaysTestCase as EveryskLibDateMixinGetHolidaysTestCase
from everysk.core.datetime.tests.calendar import CalendarTestCase as EveryskLibCalendarTestCase

## Exceptions Test Cases
from everysk.core._tests.exceptions import (
    BaseExceptionTestCase as EveryskLibBaseExceptionTestCase, DefaultErrorTestCase as EveryskLibDefaultErrorTestCase,
    HttpErrorTestCase as EveryskLibHttpErrorTestCase, FieldValueErrorTestCase as EveryskLibFieldValueErrorTestCase,
    ReadonlyErrorTestCase as EveryskLibReadonlyErrorTestCase, RequiredErrorTestCase as EveryskLibRequiredErrorTestCase
)

## Fields Test Cases
from everysk.core._tests.fields import (
    BoolFieldTestCase as EveryskLibBoolFieldTestCase, ChoiceFieldTestCase as EveryskLibChoiceFieldTestCase, DateFieldTestCase as EveryskLibDateFieldTestCase,
    DateTimeFieldTestCase as EveryskLibDateTimeFieldTestCase, DictFieldTestCase as EveryskLibDictFieldTestCase, FieldTestCase as EveryskLibFieldTestCase,
    FieldUndefinedTestCase as EveryskLibFieldUndefinedTestCase, FloatFieldTestCase as EveryskLibFloatFieldTestCase, IntFieldTestCase as EveryskLibIntFieldTestCase,
    IteratorFieldTestCase as EveryskLibIteratorFieldTestCase, ListFieldTestCase as EveryskLibListFieldTestCase, ReadonlyDictFieldTestCase as EveryskLibReadonlyDictFieldTestCase,
    ReadonlyListFieldTestCase as EveryskLibReadonlyListFieldTestCase, StrFieldTestCase as EveryskLibStrFieldTestCase, TupleFieldTestCase as EveryskLibTupleFieldTestCase,
    ObjectInitPropertyTestCase as EveryskLibObjectInitPropertyTestCase, COD3770TestCase as EveryskLibCOD3770TestCase
)

## Firestore Test Cases
try:
    from everysk.core._tests.firestore import (
        BaseDocumentCachedConfigTestCase as EveryskLibBaseDocumentCachedConfigTestCase,
        BaseDocumentConfigTestCase as EveryskLibBaseDocumentConfigTestCase,
        DocumentCachedTestCase as EveryskLibDocumentCachedTestCase,
        DocumentTestCase as EveryskLibDocumentTestCase,
        FirestoreClientTestCase as EveryskLibFirestoreClientTestCase,
        LoadsPaginatedTestCase as EveryskLibLoadsPaginatedTestCase
    )
except ModuleNotFoundError as error:
    # This will prevent running these tests if google-cloud-firestore is not installed
    if not error.args[0].startswith("No module named 'google'"):
        raise error

## Http Test Cases
try:
    from everysk.core._tests.http import (
        HttpConnectionTestCase as EveryskLibHttpConnectionTestCase,
        HttpGETConnectionTestCase as EveryskLibHttpGETConnectionTestCase,
        HttpPOSTConnectionTestCase as EveryskLibHttpPOSTConnectionTestCase
    )
except ModuleNotFoundError as error:
    # This will prevent running these tests if requests is not installed
    if not error.args[0].startswith("No module named 'requests'"):
        raise error

## Log Test Cases
from everysk.core._tests.log import (
    LoggerTestCase as EveryskLibLoggerTestCase,
    LoggerDeprecatedTestCase as EveryskLibLoggerDeprecatedTestCase,
    LoggerManagerTestCase as EveryskLibLoggerManagerTestCase,
    LoggerSlackTestCase as EveryskLibLoggerSlackTestCase
)


## Object Test Cases
from everysk.core._tests.object import (
    BaseDictPropertyTestCase as EveryskLibBaseDictPropertyTestCase, BaseDictTestCase as EveryskLibBaseDictTestCase,
    BaseFieldTestCase as EveryskLibBaseFieldTestCase, BaseObjectTestCase as EveryskLibBaseObjectTestCase,
    ConfigHashTestCase as EveryskLibConfigHashTestCase, FrozenDictTestCase as EveryskLibFrozenDictTestCase,
    FrozenObjectTestCase as EveryskLibFrozenObjectTestCase, MetaClassConfigTestCase as EveryskLibMetaClassConfigTestCase,
    RequiredTestCase as EveryskLibRequiredTestCase, ValidateTestCase as EveryskLibValidateTestCase,
    MetaClassAttributesTestCase as EveryskLibMetaClassAttributesTestCase
)

## Number Test Cases
from everysk.core._tests.number import NumberTestCase as EveryskLibNumberTestCase

## String Test Cases
from everysk.core._tests.string import StringTestCase as EveryskLibStringTestCase

## Redis Test Cases
try:
    from everysk.core._tests.redis import (
        RedisCacheCompressedTestCase as EveryskLibRedisCacheCompressedTestCase,
        RedisCacheTestCase as EveryskLibRedisCacheTestCase, RedisChannelTestCase as EveryskLibRedisChannelTestCase,
        RedisClientTestCase as EveryskLibRedisClientTestCase, RedisListTestCase as EveryskLibRedisListTestCase,
        RedisLockTestCase as EveryskLibRedisLockTestCase, RedisCacheGetSetTestCase as EveryskLibRedisCacheGetSetTestCase
    )
except ModuleNotFoundError as error:
    # This will prevent running these tests if redis is not installed
    if not error.args[0].startswith("No module named 'redis'"):
        raise error

## Slack Test Cases
try:
    from everysk.core._tests.slack import SlackTestCase as EveryskLibSlackTestCase
except ModuleNotFoundError as error:
    # This will prevent running these tests if requests is not installed
    if not error.args[0].startswith("No module named 'requests'"):
        raise error

## Thread Test Cases
from everysk.core._tests.threads import ThreadPoolTestCase as EveryskLibThreadPoolTestCase, ThreadTestCase as EveryskLibThreadTestCase

## Undefined Test Cases
from everysk.core._tests.undefined import UndefinedTestCase as EveryskLibUndefinedTestCase

## Utils Test Cases
from everysk.core._tests.utils import (
    BoolConverterTestCase as EveryskLibBoolConverterTestCase,
    SearchKeyTestCase as EveryskLibSearchKeyTestCase
)

## Workers Test Cases
try:
    from everysk.core._tests.workers import (
        BaseGoogleTestCase as EveryskLibBaseGoogleTestCase,
        TaskGoogleTestCase as EveryskLibTaskGoogleTestCase,
        WorkerGoogleTestCase as EveryskLibWorkerGoogleTestCase
    )
except ModuleNotFoundError as error:
    # This will prevent running these tests if google-cloud-tasks is not installed
    if not error.args[0].startswith("No module named 'google'"):
        raise error
