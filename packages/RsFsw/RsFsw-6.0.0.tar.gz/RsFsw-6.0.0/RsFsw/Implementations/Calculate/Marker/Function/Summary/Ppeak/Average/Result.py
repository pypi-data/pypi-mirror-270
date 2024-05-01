from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:SUMMary:PPEak:AVERage:RESult \n
		Snippet: value: float = driver.calculate.marker.function.summary.ppeak.average.result.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Queries the average positive peak time domain power. The query is only possible if averaging has been activated
		previously using method RsFsw.Calculate.Marker.Function.Summary.Average.set. To get a valid result, you have to perform a
		complete measurement with synchronization to the end of the measurement before reading out the result. This is only
		possible for single sweep mode. See also method RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: peak_power: Peak power of the signal during the measurement time."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:SUMMary:PPEak:AVERage:RESult?')
		return Conversions.str_to_float(response)
