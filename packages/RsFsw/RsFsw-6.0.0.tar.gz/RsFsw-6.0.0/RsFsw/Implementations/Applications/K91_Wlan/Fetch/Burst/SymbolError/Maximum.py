from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:SYMBolerror:MAXimum \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.symbolError.maximum.get() \n
		Returns the average, maximum or minimum percentage of symbols that were outside the allowed demodulation range within a
		PPDU (as defined by the standard) . For details see 'Modulation accuracy, flatness and tolerance parameters'. \n
			:return: result: Global Result, Stream 1 result ... Stream n result"""
		response = self._core.io.query_str(f'FETCh:BURSt:SYMBolerror:MAXimum?')
		return trim_str_response(response)
