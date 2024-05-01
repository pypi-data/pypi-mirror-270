from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class YCls:
	"""Y commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: CALCulate<n>:DISTribution:Y \n
		Snippet: value: str = driver.applications.k60Transient.calculate.distribution.y.get(window = repcap.Window.Default) \n
		Queries the y-axis values of the specified Parameter Distribution display. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: yaxis: char_data The number of values is defined by method RsFsw.Applications.K6_Pulse.Calculate.Distribution.Nbins.set. The used unit depends on the selected parameter."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DISTribution:Y?')
		return trim_str_response(response)
