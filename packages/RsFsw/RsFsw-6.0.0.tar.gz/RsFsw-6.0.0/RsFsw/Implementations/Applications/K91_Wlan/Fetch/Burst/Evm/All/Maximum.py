from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:EVM:ALL:MAXimum \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.evm.all.maximum.get() \n
		Returns the average, maximum or minimum EVM in dB. This is a combined figure that represents the pilot, data and the free
		carrier. For details see 'Modulation accuracy, flatness and tolerance parameters'. \n
			:return: result: Global Result, Stream 1 result ... Stream n result"""
		response = self._core.io.query_str(f'FETCh:BURSt:EVM:ALL:MAXimum?')
		return trim_str_response(response)
