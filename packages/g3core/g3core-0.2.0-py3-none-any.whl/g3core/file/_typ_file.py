from dataclasses import dataclass

from ._base_file import BaseFile
from ..st_parser import STStruct, STIntEnum


@dataclass(frozen=True)
class TypFile(BaseFile):
    """A wrapper around a `.typ` SystemG3Core file.

    Attributes:
        contents (str): The contents of the file.
    """

    def get_struct(self, struct_name: str) -> STStruct:
        """Get a struct wrapper from the file.

        Args:
            struct_name (str): The name of the struct to get.

        Returns:
            STStruct: The struct wrapper object.
        """
        fb_contents = self._get_structure(
            structure_name=struct_name,
            structure_type='Struct',
            search_pattern=f'(^\\s*{struct_name}\\s*:\\s*STRUCT.*?END_STRUCT)',
            )
        return STStruct(fb_contents)

    def get_int_enum(self, enum_name: str) -> STIntEnum:
        """Get an integer enum wrapper from the file.

        Args:
            enum_name (str): The name of the integer enum to get.

        Returns:
            STIntEnum: The integer enum wrapper object.
        """
        e_contents = self._get_structure(
            structure_name=enum_name,
            structure_type='Enum',
            search_pattern=f"^\\s*{enum_name}\\s*:\\s*\\(.*?\\);",
            )
        return STIntEnum(e_contents)
