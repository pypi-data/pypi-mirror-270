from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SizeCls:
	"""Size commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("size", core, parent)

	def set(self, max_no_peaks: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:FPEaks:LIST:SIZE \n
		Snippet: driver.applications.k14Xnr5G.calculate.marker.function.fpeaks.listPy.size.set(max_no_peaks = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Defines the maximum number of peaks that the FSW looks for during a peak search. \n
			:param max_no_peaks: Maximum number of peaks to be determined. Range: 1 to 500
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(max_no_peaks)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:FPEaks:LIST:SIZE {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:FPEaks:LIST:SIZE \n
		Snippet: value: float = driver.applications.k14Xnr5G.calculate.marker.function.fpeaks.listPy.size.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Defines the maximum number of peaks that the FSW looks for during a peak search. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: max_no_peaks: Maximum number of peaks to be determined. Range: 1 to 500"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:FPEaks:LIST:SIZE?')
		return Conversions.str_to_float(response)
