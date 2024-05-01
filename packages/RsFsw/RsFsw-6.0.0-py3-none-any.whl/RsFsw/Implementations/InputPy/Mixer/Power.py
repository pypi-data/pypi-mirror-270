from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: float) -> None:
		"""SCPI: INPut:MIXer[:POWer] \n
		Snippet: driver.inputPy.mixer.power.set(power = 1.0) \n
		No command help available \n
			:param power: No help available
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'INPut:MIXer:POWer {param}')

	def get(self) -> float:
		"""SCPI: INPut:MIXer[:POWer] \n
		Snippet: value: float = driver.inputPy.mixer.power.get() \n
		No command help available \n
			:return: power: No help available"""
		response = self._core.io.query_str(f'INPut:MIXer:POWer?')
		return Conversions.str_to_float(response)
