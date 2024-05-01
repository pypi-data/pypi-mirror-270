from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MarginCls:
	"""Margin commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("margin", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:EVM:XCORrelation:MARGin \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.evm.xcorrelation.margin.get() \n
		No command help available \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'FETCh:BURSt:EVM:XCORrelation:MARGin?')
		return trim_str_response(response)
