from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LengthsCls:
	"""Lengths commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lengths", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:LENGths \n
		Snippet: value: str = driver.applications.k9X11Ad.fetch.burst.lengths.get() \n
		Returns the length of the analyzed PPDUs from the current measurement. If the number of PPDUs to analyze is greater than
		the number of PPDUs that can be captured in one buffer, this command only returns the lengths of the PPDUs in the current
		capture buffer. The result is a comma-separated list of lengths, one for each PPDU. \n
			:return: ppdu_length: Length of the PPDU in the unit specified by the method RsFsw.Applications.K91_Wlan.Unit.Burst.set command. Tip: To obtain the result in seconds, divide the number of samples by the input sample rate. This value is indicated as 'Sample Rate Fs' in the channel bar."""
		response = self._core.io.query_str(f'FETCh:BURSt:LENGths?')
		return trim_str_response(response)
