import logging
import typing
import re

from dataclasses import dataclass, field


logger = logging.getLogger('g3core.st_parser')


class STToPyConverter:
    """
    Utility class for converting Structured Text values to Python data types.
    """

    @staticmethod
    def _bool_to_py(value: typing.Any) -> bool:
        return str(value).casefold() == 'true'

    @staticmethod
    def _byte_to_py(value: typing.Any) -> int:
        return int(value)

    @staticmethod
    def _word_to_py(value: typing.Any) -> int:
        return int(value)

    @staticmethod
    def _int_to_py(value: typing.Any) -> int:
        return int(value)

    @staticmethod
    def _real_to_py(value: typing.Any) -> float:
        return float(value)

    @staticmethod
    def _char_to_py(value: typing.Any) -> str:
        return str(value)

    @staticmethod
    def _string_to_py(value: typing.Any) -> str:
        return str(value)

    @staticmethod
    def _enum_to_py(value: typing.Any) -> str:
        return str(value)

    @staticmethod
    def _time_to_py(value: typing.Any) -> str:
        time_pattern = r'^(T#)?(\d+d)?(\d+h)?(\d+m)?(\d+s)?(\d+ms)?$'
        match = re.match(time_pattern, str(value))
        if not match:
            raise ValueError(f"Invalid TIME variable: {value}")
        if match.group(1):
            return value
        if not value:
            raise ValueError("TIME variable is an empty string")
        return f"T#{value}"  # add the T# prefix if not present

    @classmethod
    def _array_to_py(cls, value: typing.Any) -> str:
        raise NotImplementedError("Array parsing is not supported yet.")

    @classmethod
    def _struct_to_py(cls, value: typing.Any) -> dict:
        raise NotImplementedError("Struct parsing is not supported yet.")

    @classmethod
    def to_py(cls, value: typing.Any, dtype: str) -> typing.Any:
        """Convert an ST value to a Python data type.

        Args:
            value (typing.Any): The Structured Text value to convert.
            dtype (str): The Structured Text data type of the value.

        Raises:
            ValueError: If the data type is not supported.

        Returns:
            typing.Any: The converted value.
        """
        if value is None:
            return None
        dtype_lower = dtype.lower()
        if "array" in dtype_lower:
            return cls._array_to_py(value)
        elif "struct" in dtype_lower:
            return cls._struct_to_py(value)
        elif "enum" in dtype_lower:
            return cls._enum_to_py(value)
        elif "bool" == dtype_lower:
            return cls._bool_to_py(value)
        elif "byte" == dtype_lower:
            return cls._byte_to_py(value)
        elif "word" == dtype_lower:
            return cls._word_to_py(value)
        elif "int" in dtype_lower:
            return cls._int_to_py(value)
        elif "real" in dtype_lower:
            return cls._real_to_py(value)
        elif "char" == dtype_lower:
            return cls._char_to_py(value)
        elif "string" in dtype_lower:
            return cls._string_to_py(value)
        elif "time" in dtype_lower:
            return cls._time_to_py(value)
        else:
            raise ValueError(f'Unsupported data type: "{dtype}"')


def to_py(value: typing.Any, dtype: str) -> typing.Any:
    """Convert a Structured Text value to a Python data type.

    Args:
        value (typing.Any): The Structured Text value to convert.
        dtype (str): The Structured Text data type of the value.

    Returns:
        typing.Any: The converted value.
    """
    return STToPyConverter.to_py(value, dtype)


@dataclass
class STVariable:
    """Structured Text variable.

    Attributes:
        name (str): The name of the variable.
        dtype (str): The ST data type of the variable.
        value (typing.Any): The ST value of the variable.
        default (typing.Any | None, optional): The default value of\
            the variable. Defaults to None.
        comment (str | None, optional): The comment for the variable.\
            Defaults to None.
    """
    name: str
    """The name of the variable."""
    dtype: str
    """The ST data type of the variable."""
    value: typing.Any
    """The ST value of the variable."""
    default: typing.Any | None = field(default=None, repr=False)
    """The default ST value of the variable."""
    comment: str | None = field(default=None, repr=False)
    """The comment for the variable."""

    def __post_init__(self) -> None:
        self._check_name(self.name)

    def __str__(self) -> str:
        return str(self.to_py())

    @staticmethod
    def _check_name(name) -> None:
        if not isinstance(name, str):
            raise ValueError('Varname must be a string value.')
        if not name:
            raise ValueError('Varname cannot be an empty string.')
        if not name[0].isalpha():
            raise ValueError('Varname must start with a letter.')
        if any(not ch.isalnum() and ch != '_' for ch in name):
            raise ValueError(
                'Varname may only contain alphanumeric values and underscores.'
                )

    def to_py(self) -> typing.Any:
        """Convert the Structured Text value to a Python data type.
        If the conversion fails, the default value will be converted instead.
        If the default value is the same as the value, or the default value
        conversion fails, the value will be returned as-is.

        Returns:
            typing.Any: The converted value.
        """
        try:
            return STToPyConverter.to_py(self.value, self.dtype)
        except Exception as exp:
            if self.default != self.value:
                logger.warning(
                    '"%s": failed to format value "%s" to data type "%s" '
                    '(%s). Default value "%s" will be formatted instead.',
                    self.name,
                    self.value if self.value != '' else '<empty str>',
                    self.dtype,
                    exp,
                    self.default if self.default != '' else '<empty str>'
                    )
                try:
                    return STToPyConverter.to_py(self.default, self.dtype)
                except Exception as exp_:
                    logger.error(
                        '"%s": failed to format default value "%s" to '
                        'data type "%s" (%s). Value "%s" will be used as-is.',
                        self.name,
                        self.default if self.default != '' else '<empty str>',
                        self.dtype,
                        exp_,
                        self.value if self.value != '' else '<empty str>'
                        )
                    return self.value
            else:
                logger.warning(
                    '"%s": failed to format value "%s" to data type "%s" '
                    '(%s). Value will be used as-is.',
                    self.name,
                    self.value if self.value != '' else '<empty str>',
                    self.dtype,
                    exp
                    )
                return self.value
