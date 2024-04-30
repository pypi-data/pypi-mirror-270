import re

from dataclasses import dataclass
from functools import cached_property

from ._st_var import STVariable
from ._st_base_structure import STBaseStructure


@dataclass
class STFunction(STBaseStructure):
    """Structured Text function structure.

    Attributes:
        contents (str): The contents of the function.
    """

    def _extract_name(self) -> str:
        name = re.search(r"FUNCTION\s+(\w+)", self.contents)
        if not name:
            raise TypeError('Cannot parse the name of the function.')
        return name.group(1)

    def _instantiate(self, varname: str) -> str:
        return f'f{varname}:{self.name}'

    @cached_property
    def return_type(self) -> str:
        """The return type of the function."""
        match = re.search(r"FUNCTION\s+.*? :\s+(\w+)", self.contents)
        if not match:
            raise TypeError('Cannot parse return type of the function.')
        return match.group(1)

    @cached_property
    def var_input(self) -> list[STVariable]:
        """The input variables (`VAR_INPUT`) of the function."""
        return self._parse_section('VAR_INPUT', 'END_VAR')


@dataclass
class STFunctionBlock(STBaseStructure):
    """Structured Text function block structure.

    Attributes:
        contents (str): The contents of the function block.
    """

    def _extract_name(self) -> str:
        name = re.search(r"FUNCTION_BLOCK\s+(\w+)", self.contents)
        if not name:
            raise TypeError('Cannot parse the name of the function block.')
        return name.group(1)

    def _instantiate(self, varname: str) -> str:
        return f'fb{varname}:{self.name}'

    @cached_property
    def var_in_out(self) -> list[STVariable]:
        """The input/output variables (`VAR_IN_OUT`) of the function block."""
        return self._parse_section('VAR_IN_OUT', 'END_VAR')

    @cached_property
    def var_input(self) -> list[STVariable]:
        """The input variables (`VAR_INPUT`) of the function block."""
        return self._parse_section('VAR_INPUT', 'END_VAR')

    @cached_property
    def var_out(self) -> list[STVariable]:
        """The output variables (`VAR_OUTPUT`) of the function block."""
        return self._parse_section('VAR_OUT', 'END_VAR')

    @cached_property
    def var(self) -> list[STVariable]:
        """The inner variables (`VAR`) of the function block."""
        return self._parse_section('VAR', 'END_VAR')
