from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:BURSt:COUNt \n
		Snippet: value: float = driver.applications.k9X11Ad.fetch.burst.count.get() \n
		Returns the number of analyzed PPDUs from the current capture buffer. If multiple measurements are required because the
		number of PPDUs to analyze is greater than the number of PPDUs that can be captured in one buffer, this command only
		returns the number of captured PPDUs in the current capture buffer (as opposed to method RsFsw.Applications.K91_Wlan.
		Fetch.Burst.Count.All.get_) . \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'FETCh:BURSt:COUNt?')
		return Conversions.str_to_float(response)
