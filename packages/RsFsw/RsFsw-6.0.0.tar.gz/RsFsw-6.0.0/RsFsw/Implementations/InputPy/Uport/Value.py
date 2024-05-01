from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ValueCls:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def get(self) -> float:
		"""SCPI: INPut:UPORt[:VALue] \n
		Snippet: value: float = driver.inputPy.uport.value.get() \n
		Queries the control lines of the user ports. For details see method RsFsw.Output.Uport.Value.set. \n
			:return: level: bit values in hexadecimal format TTL type voltage levels (max. 5V) Range: #B00000000 to #B00111111"""
		response = self._core.io.query_str(f'INPut:UPORt:VALue?')
		return Conversions.str_to_float(response)
