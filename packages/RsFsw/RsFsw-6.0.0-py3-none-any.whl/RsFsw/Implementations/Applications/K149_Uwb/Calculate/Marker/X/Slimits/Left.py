from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LeftCls:
	"""Left commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("left", core, parent)

	def set(self, arg_0: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:X:SLIMits:LEFT \n
		Snippet: driver.applications.k149Uwb.calculate.marker.x.slimits.left.set(arg_0 = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Defines the left limit of the marker search range for all markers in all windows. If you perform a measurement in the
		time domain, this command limits the range of the trace to be analyzed. \n
			:param arg_0: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:X:SLIMits:LEFT {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:X:SLIMits:LEFT \n
		Snippet: value: float = driver.applications.k149Uwb.calculate.marker.x.slimits.left.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Defines the left limit of the marker search range for all markers in all windows. If you perform a measurement in the
		time domain, this command limits the range of the trace to be analyzed. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: arg_0: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:X:SLIMits:LEFT?')
		return Conversions.str_to_float(response)
