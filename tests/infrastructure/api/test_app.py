import unittest

from parameterized import parameterized
from pydantic import BaseModel


class InitTestConfig(BaseModel):
    pass


class AppTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand(
        [
            [
                "sanity",
                InitTestConfig(
                    ...
                )
            ]
        ]
    )
    def test_init(self, name: str, config: InitTestConfig):
        pass
