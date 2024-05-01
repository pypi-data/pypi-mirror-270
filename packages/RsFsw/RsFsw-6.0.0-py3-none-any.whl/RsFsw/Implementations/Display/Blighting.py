from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BlightingCls:
	"""Blighting commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("blighting", core, parent)

	def set(self, brightness: float) -> None:
		"""SCPI: DISPlay:BLIGhting \n
		Snippet: driver.display.blighting.set(brightness = 1.0) \n
		No command help available \n
			:param brightness: No help available
		"""
		param = Conversions.decimal_value_to_str(brightness)
		self._core.io.write(f'DISPlay:BLIGhting {param}')

	def get(self) -> float:
		"""SCPI: DISPlay:BLIGhting \n
		Snippet: value: float = driver.display.blighting.get() \n
		No command help available \n
			:return: brightness: No help available"""
		response = self._core.io.query_str(f'DISPlay:BLIGhting?')
		return Conversions.str_to_float(response)
