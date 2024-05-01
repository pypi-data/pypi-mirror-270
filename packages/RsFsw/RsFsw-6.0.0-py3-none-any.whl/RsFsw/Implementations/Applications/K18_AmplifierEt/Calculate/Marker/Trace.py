from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TraceCls:
	"""Trace commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	def set(self, trace: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:TRACe \n
		Snippet: driver.applications.k18AmplifierEt.calculate.marker.trace.set(trace = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Selects the trace the marker is positioned on. Note that the corresponding trace must have a trace mode other than
		'Blank'. If necessary, the command activates the marker first. \n
			:param trace: 1 to 4 Trace number the marker is assigned to. MAXHold Marker is assigned to maxhold trace of persistent spectrum (only available in Persistent Spectrum window) WRITe Marker is assigned to clear/write trace of persistent spectrum (only available in Persistent Spectrum window)
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(trace)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:TRACe {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:TRACe \n
		Snippet: value: float = driver.applications.k18AmplifierEt.calculate.marker.trace.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Selects the trace the marker is positioned on. Note that the corresponding trace must have a trace mode other than
		'Blank'. If necessary, the command activates the marker first. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: trace: 1 to 4 Trace number the marker is assigned to. MAXHold Marker is assigned to maxhold trace of persistent spectrum (only available in Persistent Spectrum window) WRITe Marker is assigned to clear/write trace of persistent spectrum (only available in Persistent Spectrum window)"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:TRACe?')
		return Conversions.str_to_float(response)
