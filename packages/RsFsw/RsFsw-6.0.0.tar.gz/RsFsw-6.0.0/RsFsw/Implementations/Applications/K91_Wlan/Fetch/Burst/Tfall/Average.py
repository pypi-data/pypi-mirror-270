from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:TFALl:AVERage \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.tfall.average.get() \n
		Returns the average, maximum or minimum PPDU fall time in seconds. Is only applicable to IEEE802.11b & IEEE802.11g (DSSS)
		signals. For details see 'Modulation accuracy, flatness and tolerance parameters'. \n
			:return: result: list"""
		response = self._core.io.query_str(f'FETCh:BURSt:TFALl:AVERage?')
		return trim_str_response(response)
