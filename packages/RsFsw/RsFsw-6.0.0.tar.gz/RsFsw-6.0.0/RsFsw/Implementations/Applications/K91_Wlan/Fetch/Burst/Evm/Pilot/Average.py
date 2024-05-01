from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:EVM:PILot:AVERage \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.evm.pilot.average.get() \n
		Returns the average, maximum or minimum EVM in dB for the pilot carrier. For details see 'Modulation accuracy, flatness
		and tolerance parameters'. \n
			:return: result: Global Result, Stream 1 result ... Stream n result"""
		response = self._core.io.query_str(f'FETCh:BURSt:EVM:PILot:AVERage?')
		return trim_str_response(response)
