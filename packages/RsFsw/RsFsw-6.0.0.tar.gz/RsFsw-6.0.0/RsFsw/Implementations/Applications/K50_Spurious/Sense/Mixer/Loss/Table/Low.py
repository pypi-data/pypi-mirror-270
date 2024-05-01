from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowCls:
	"""Low commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("low", core, parent)

	def set(self, table_low: str) -> None:
		"""SCPI: [SENSe]:MIXer:LOSS:TABLe[:LOW] \n
		Snippet: driver.applications.k50Spurious.sense.mixer.loss.table.low.set(table_low = 'abc') \n
		Defines the file name of the conversion loss table to be used for the low (first) range. \n
			:param table_low: No help available
		"""
		param = Conversions.value_to_quoted_str(table_low)
		self._core.io.write(f'SENSe:MIXer:LOSS:TABLe:LOW {param}')

	def get(self, table_low: str) -> str:
		"""SCPI: [SENSe]:MIXer:LOSS:TABLe[:LOW] \n
		Snippet: value: str = driver.applications.k50Spurious.sense.mixer.loss.table.low.get(table_low = 'abc') \n
		Defines the file name of the conversion loss table to be used for the low (first) range. \n
			:param table_low: No help available
			:return: table_low: No help available"""
		param = Conversions.value_to_quoted_str(table_low)
		response = self._core.io.query_str(f'SENSe:MIXer:LOSS:TABLe:LOW? {param}')
		return trim_str_response(response)
