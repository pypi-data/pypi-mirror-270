from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ValueCls:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, subcarrier_spacing_value: float) -> None:
		"""SCPI: CONFigure:WLAN:SSPacing:VALue \n
		Snippet: driver.applications.k91Wlan.configure.wlan.sspacing.value.set(subcarrier_spacing_value = 1.0) \n
		No command help available \n
			:param subcarrier_spacing_value: No help available
		"""
		param = Conversions.decimal_value_to_str(subcarrier_spacing_value)
		self._core.io.write(f'CONFigure:WLAN:SSPacing:VALue {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:WLAN:SSPacing:VALue \n
		Snippet: value: float = driver.applications.k91Wlan.configure.wlan.sspacing.value.get() \n
		No command help available \n
			:return: subcarrier_spacing_value: No help available"""
		response = self._core.io.query_str(f'CONFigure:WLAN:SSPacing:VALue?')
		return Conversions.str_to_float(response)
