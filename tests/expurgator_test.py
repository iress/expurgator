import pytest

from expurgator import shallow_dict_expurgator


class TestExpurgator(object):
    """Tests for expurgator"""

    def test_shallow_dict_expurgator(self):
        # setup
        obj = {
            "password": "hunter2",
            "walk": "this way",
            "sessionid": [1, 2],
        }

        # exercise
        result = shallow_dict_expurgator(obj)

        # verify
        assert result == {
            "password": "<SensitiveString>",
            "walk": "this way",
            "sessionid": [1, 2],
        }
