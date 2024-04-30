import re

from dataclasses import dataclass
from functools import cached_property

from ._st_var import STVariable
from ._st_base_structure import STBaseStructure


@dataclass
class STStruct(STBaseStructure):
    """Structured Text struct structure.

    Attributes:
        contents (str): The contents of the struct.
    """

    def _extract_name(self) -> str:
        name = re.search(r"^\s*(\w+)\s*:\s*STRUCT", self.contents)
        if not name:
            raise TypeError('Cannot parse the name of the struct.')
        return name.group(1)

    def _instantiate(self, varname: str, **config_params: str) -> str:
        raise NotImplementedError("Struct instantiation is not supported yet.")

    @cached_property
    def members(self) -> list[STVariable]:
        """The members of the struct."""
        return self._parse_section('STRUCT', 'END_STRUCT')
