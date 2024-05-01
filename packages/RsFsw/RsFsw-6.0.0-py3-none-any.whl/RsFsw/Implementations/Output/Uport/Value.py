from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ValueCls:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, value: str) -> None:
		"""SCPI: OUTPut:UPORt[:VALue] \n
		Snippet: driver.output.uport.value.set(value = rawAbc) \n
		Sets the control lines of the user ports. The assignment of the pin numbers to the bits is as follows:
			Table Header: Bit / 7 / 6 / 5 / 4 / 3 / 2 / 1 / 0 \n
			- Pin / N/A / N/A / 5 / 3 / 4 / 7 / 6 / 2
		Bits 7 and 6 are not assigned to pins and must always be 0. The user port is written to with the given binary pattern. If
		the user port is programmed to input instead of output (see method RsFsw.InputPy.Uport.State.set) , the output value is
		temporarily stored. \n
			:param value: bit values in hexadecimal format TTL type voltage levels (max. 5V) Range: #B00000000 to #B00111111
		"""
		param = Conversions.value_to_str(value)
		self._core.io.write(f'OUTPut:UPORt:VALue {param}')

	def get(self) -> str:
		"""SCPI: OUTPut:UPORt[:VALue] \n
		Snippet: value: str = driver.output.uport.value.get() \n
		Sets the control lines of the user ports. The assignment of the pin numbers to the bits is as follows:
			Table Header: Bit / 7 / 6 / 5 / 4 / 3 / 2 / 1 / 0 \n
			- Pin / N/A / N/A / 5 / 3 / 4 / 7 / 6 / 2
		Bits 7 and 6 are not assigned to pins and must always be 0. The user port is written to with the given binary pattern. If
		the user port is programmed to input instead of output (see method RsFsw.InputPy.Uport.State.set) , the output value is
		temporarily stored. \n
			:return: value: bit values in hexadecimal format TTL type voltage levels (max. 5V) Range: #B00000000 to #B00111111"""
		response = self._core.io.query_str(f'OUTPut:UPORt:VALue?')
		return trim_str_response(response)
