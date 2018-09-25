__version__ = '0.1.1'


from six import iteritems, string_types, text_type


# names of variables that should always be hidden (lower case only)
COMMON_SENSITIVE_VARIABLE_NAMES = (
    'pass',
    'pw',
    'secret',
    'app_id',
    'token',
    'session_key',
    'sessionkey',
)


def is_sensitive_name(name, sensitive_variable_names=None):
    name_lower = name.lower()
    sensitive_names = (
        sensitive_variable_names if sensitive_variable_names is not None
        else COMMON_SENSITIVE_VARIABLE_NAMES)
    return any(v in name_lower for v in sensitive_names)


class SensitiveString(text_type):
    """A subclass of string with repr suppressed, use with passwords"""

    def __repr__(self):
        return "<SensitiveString>"


def shallow_key_value_expurgator(
        key, value, sensitive_variable_names=None):
    """Ensure that the key and value do not contain sensitive data

    Args:
        key (any): The key to check
        value (any): The value to censor
        sensitive_variable_names (Optional[list]): names of variables to
            censor (defaults to COMMON_SENSITIVE_VARIABLE_NAMES)

    Returns: value
    """
    if isinstance(key, string_types) and \
            isinstance(value, string_types) and \
            is_sensitive_name(
                key, sensitive_variable_names=sensitive_variable_names):
        return repr(SensitiveString(value))

    return value


def shallow_dict_expurgator(obj, sensitive_variable_names=None):
    """Ensure that any items coming through don't have sensitive data.

    Doing a shallow traversal on purpose.

    Args:
        obj (Mapping): the obj to check and encode
        sensitive_variable_names (Optional[list]): names of variables to
            censor (defaults to COMMON_SENSITIVE_VARIABLE_NAMES)

    Returns: Mapping
    """
    safe_dict = {}
    for key, value in iteritems(obj):
        safe_dict[key] = shallow_key_value_expurgator(
            key, value,
            sensitive_variable_names=sensitive_variable_names)

    return safe_dict
