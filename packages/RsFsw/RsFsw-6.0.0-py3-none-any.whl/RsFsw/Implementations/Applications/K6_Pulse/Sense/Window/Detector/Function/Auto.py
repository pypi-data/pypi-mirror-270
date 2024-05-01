from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: [SENSe][:WINDow<n>]:DETector<t>[:FUNCtion]:AUTO \n
		Snippet: driver.applications.k6Pulse.sense.window.detector.function.auto.set(state = False, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Couples and decouples the detector to the trace mode. \n
			:param state: ON | OFF | 0 | 1
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'SENSe:WINDow{window_cmd_val}:DETector{trace_cmd_val}:FUNCtion:AUTO {param}')

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> bool:
		"""SCPI: [SENSe][:WINDow<n>]:DETector<t>[:FUNCtion]:AUTO \n
		Snippet: value: bool = driver.applications.k6Pulse.sense.window.detector.function.auto.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Couples and decouples the detector to the trace mode. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
			:return: state: ON | OFF | 0 | 1"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'SENSe:WINDow{window_cmd_val}:DETector{trace_cmd_val}:FUNCtion:AUTO?')
		return Conversions.str_to_bool(response)
