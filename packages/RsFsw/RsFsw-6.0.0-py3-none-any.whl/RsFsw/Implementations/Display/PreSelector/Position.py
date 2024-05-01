from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PositionCls:
	"""Position commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("position", core, parent)

	def set(self, position: enums.DisplayPosition) -> None:
		"""SCPI: DISPlay:PRESelector:POSition \n
		Snippet: driver.display.preSelector.position.set(position = enums.DisplayPosition.BOTTom) \n
		No command help available \n
			:param position: No help available
		"""
		param = Conversions.enum_scalar_to_str(position, enums.DisplayPosition)
		self._core.io.write(f'DISPlay:PRESelector:POSition {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DisplayPosition:
		"""SCPI: DISPlay:PRESelector:POSition \n
		Snippet: value: enums.DisplayPosition = driver.display.preSelector.position.get() \n
		No command help available \n
			:return: position: No help available"""
		response = self._core.io.query_str(f'DISPlay:PRESelector:POSition?')
		return Conversions.str_to_scalar_enum(response, enums.DisplayPosition)
