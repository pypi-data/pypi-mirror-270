from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:FUNCtion:FIXed[:STATe] \n
		Snippet: driver.applications.k91Wlan.calculate.deltaMarker.function.fixed.state.set(state = False, window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		Activates or deactivates a marker that defines a fixed reference point for relative marker analysis. If necessary, the
		command activates a marker and positions it on the peak power. Subsequently, you can change the coordinates of the fixed
		reference independent of the marker. The fixed reference is independent of the trace and is applied to all active delta
		markers. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:FUNCtion:FIXed:STATe {param}')

	def get(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> bool:
		"""SCPI: CALCulate<n>:DELTamarker<m>:FUNCtion:FIXed[:STATe] \n
		Snippet: value: bool = driver.applications.k91Wlan.calculate.deltaMarker.function.fixed.state.get(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		Activates or deactivates a marker that defines a fixed reference point for relative marker analysis. If necessary, the
		command activates a marker and positions it on the peak power. Subsequently, you can change the coordinates of the fixed
		reference independent of the marker. The fixed reference is independent of the trace and is applied to all active delta
		markers. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:FUNCtion:FIXed:STATe?')
		return Conversions.str_to_bool(response)
