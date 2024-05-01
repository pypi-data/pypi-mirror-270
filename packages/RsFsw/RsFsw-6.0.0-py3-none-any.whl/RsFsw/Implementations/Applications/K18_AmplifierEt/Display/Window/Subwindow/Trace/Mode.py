from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, trace_mode: enums.TraceModeC, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:TRACe<t>:MODE \n
		Snippet: driver.applications.k18AmplifierEt.display.window.subwindow.trace.mode.set(trace_mode = enums.TraceModeC.AVERage, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, trace = repcap.Trace.Default) \n
		Selects the trace mode. If necessary, the selected trace is also activated. For max hold, min hold or average trace mode,
		you can set the number of single measurements with [SENSe:]SWEep:COUNt. Note that synchronization to the end of the
		measurement is possible only in single sweep mode. In the R&S FSW AM/FM/PM Modulation Analysis application, when you
		configure the traces for a window with a specific evaluation (e.g. AM time domain) , the traces in all windows with the
		same evaluation are configured identically. For more information, see 'Analyzing Several Traces - Trace Mode'. \n
			:param trace_mode: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(trace_mode, enums.TraceModeC)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:TRACe{trace_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, trace=repcap.Trace.Default) -> enums.TraceModeC:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:TRACe<t>:MODE \n
		Snippet: value: enums.TraceModeC = driver.applications.k18AmplifierEt.display.window.subwindow.trace.mode.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, trace = repcap.Trace.Default) \n
		Selects the trace mode. If necessary, the selected trace is also activated. For max hold, min hold or average trace mode,
		you can set the number of single measurements with [SENSe:]SWEep:COUNt. Note that synchronization to the end of the
		measurement is possible only in single sweep mode. In the R&S FSW AM/FM/PM Modulation Analysis application, when you
		configure the traces for a window with a specific evaluation (e.g. AM time domain) , the traces in all windows with the
		same evaluation are configured identically. For more information, see 'Analyzing Several Traces - Trace Mode'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: trace_mode: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:TRACe{trace_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TraceModeC)
