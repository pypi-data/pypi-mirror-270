from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SkewCls:
	"""Skew commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("skew", core, parent)

	def set(self, skew: float) -> None:
		"""SCPI: INPut:IQ:SKEW \n
		Snippet: driver.applications.k91Wlan.inputPy.iq.skew.set(skew = 1.0) \n
		No command help available \n
			:param skew: No help available
		"""
		param = Conversions.decimal_value_to_str(skew)
		self._core.io.write(f'INPut:IQ:SKEW {param}')

	def get(self) -> float:
		"""SCPI: INPut:IQ:SKEW \n
		Snippet: value: float = driver.applications.k91Wlan.inputPy.iq.skew.get() \n
		No command help available \n
			:return: skew: No help available"""
		response = self._core.io.query_str(f'INPut:IQ:SKEW?')
		return Conversions.str_to_float(response)
