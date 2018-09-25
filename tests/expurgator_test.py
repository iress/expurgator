import pytest

from expurgator import shallow_dict_expurgator


class TestExpurgator(object):
    """Tests for expurgator"""

    def test_shallow_dict_expurgator(self):
        """Test that sensitive dict items get censored."""
        # setup
        obj = {
            "password": "hunter2",
            "walk": "this way",
            "sessionid": [1, 2]}

        # exercise
        result = shallow_dict_expurgator(obj)

        # verify
        assert result == {
            "password": "<SensitiveString>",
            "walk": "this way",
            "sessionid": [1, 2]}

    def test_shallow_dict_expurgator_custom_name_list(self):
        """Test dict censoring with custom name list."""
        # setup
        obj = {
            "password": "1337haxx0r",
            "clandestineinfo": "re-inforcements on their way",
            "froggies": [3, 4, 5]}
        sensitive_variable_names = ['clandestineinfo', 'hushhush']

        # exercise
        result = shallow_dict_expurgator(
            obj, sensitive_variable_names=sensitive_variable_names)

        # verify
        assert result == {
            "password": "1337haxx0r",
            "clandestineinfo": "<SensitiveString>",
            "froggies": [3, 4, 5]}
