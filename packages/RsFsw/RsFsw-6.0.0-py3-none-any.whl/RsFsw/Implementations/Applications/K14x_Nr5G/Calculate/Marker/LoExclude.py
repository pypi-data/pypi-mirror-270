from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LoExcludeCls:
	"""LoExclude commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("loExclude", core, parent)

	def set(self, arg_0: bool, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:LOEXclude \n
		Snippet: driver.applications.k14Xnr5G.calculate.marker.loExclude.set(arg_0 = False, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Turns the suppression of the local oscillator during automatic marker positioning on and off (for all markers in all
		windows) . \n
			:param arg_0: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.bool_to_str(arg_0)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:LOEXclude {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> bool:
		"""SCPI: CALCulate<n>:MARKer<m>:LOEXclude \n
		Snippet: value: bool = driver.applications.k14Xnr5G.calculate.marker.loExclude.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Turns the suppression of the local oscillator during automatic marker positioning on and off (for all markers in all
		windows) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: arg_0: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:LOEXclude?')
		return Conversions.str_to_bool(response)
