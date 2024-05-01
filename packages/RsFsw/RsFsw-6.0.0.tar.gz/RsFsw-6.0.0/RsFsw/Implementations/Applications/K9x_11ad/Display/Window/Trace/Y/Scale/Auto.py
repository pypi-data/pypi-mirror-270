from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, auto: bool, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:Y[:SCALe]:AUTO \n
		Snippet: driver.applications.k9X11Ad.display.window.trace.y.scale.auto.set(auto = False, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Activates or deactivates automatic scaling of the x-axis or y-axis for the specified trace display. This command is
		currently only supported for Amplitude Modulation measurements. \n
			:param auto: ON | OFF | 0 | 1 OFF | 0 The x-axis or y-axis is scaled according to the specified minimum/maximum values (see method RsFsw.Applications.K50_Spurious.Display.Window.Trace.Y.Scale.Minimum.set/method RsFsw.Applications.K50_Spurious.Display.Window.Trace.Y.Scale.Maximum.set) and number of divisions (see method RsFsw.Applications.K91_Wlan.Display.Window.Subwindow.Trace.Y.Scale.Divisions.set) . ON | 1 The R&S FSW WLAN application automatically scales the x-axis or y-axis to best fit the measurement results.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.bool_to_str(auto)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe:AUTO {param}')

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:Y[:SCALe]:AUTO \n
		Snippet: value: bool = driver.applications.k9X11Ad.display.window.trace.y.scale.auto.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Activates or deactivates automatic scaling of the x-axis or y-axis for the specified trace display. This command is
		currently only supported for Amplitude Modulation measurements. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: auto: ON | OFF | 0 | 1 OFF | 0 The x-axis or y-axis is scaled according to the specified minimum/maximum values (see method RsFsw.Applications.K50_Spurious.Display.Window.Trace.Y.Scale.Minimum.set/method RsFsw.Applications.K50_Spurious.Display.Window.Trace.Y.Scale.Maximum.set) and number of divisions (see method RsFsw.Applications.K91_Wlan.Display.Window.Subwindow.Trace.Y.Scale.Divisions.set) . ON | 1 The R&S FSW WLAN application automatically scales the x-axis or y-axis to best fit the measurement results."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe:AUTO?')
		return Conversions.str_to_bool(response)
