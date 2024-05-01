from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FunctionCls:
	"""Function commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("function", core, parent)

	def set(self, detector: enums.DetectorE, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: [SENSe][:WINDow<n>]:DETector<t>[:FUNCtion] \n
		Snippet: driver.applications.k18AmplifierEt.sense.window.detector.function.set(detector = enums.DetectorE.AVERage, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Defines the trace detector to be used for trace analysis. For details see 'Sweep time and detector'. \n
			:param detector: NEGative Negative peak POSitive Positive peak SAMPle First value detected per trace point AVERage Average
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
		"""
		param = Conversions.enum_scalar_to_str(detector, enums.DetectorE)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'SENSe:WINDow{window_cmd_val}:DETector{trace_cmd_val}:FUNCtion {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.DetectorE:
		"""SCPI: [SENSe][:WINDow<n>]:DETector<t>[:FUNCtion] \n
		Snippet: value: enums.DetectorE = driver.applications.k18AmplifierEt.sense.window.detector.function.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Defines the trace detector to be used for trace analysis. For details see 'Sweep time and detector'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
			:return: detector: NEGative Negative peak POSitive Positive peak SAMPle First value detected per trace point AVERage Average"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'SENSe:WINDow{window_cmd_val}:DETector{trace_cmd_val}:FUNCtion?')
		return Conversions.str_to_scalar_enum(response, enums.DetectorE)
