from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Trace, default value after init: Trace.Tr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_trace_get', 'repcap_trace_set', repcap.Trace.Tr1)

	def repcap_trace_set(self, trace: repcap.Trace) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Trace.Default
		Default value after init: Trace.Tr1"""
		self._cmd_group.set_repcap_enum_value(trace)

	def repcap_trace_get(self) -> repcap.Trace:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default, trace=repcap.Trace.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:MDEPth:RESult<t> \n
		Snippet: value: float = driver.calculate.marker.function.mdepth.result.get(window = repcap.Window.Default, marker = repcap.Marker.Default, trace = repcap.Trace.Default) \n
		Queries the results of the AM modulation depth measurement.. To get a valid result, you have to perform a complete
		measurement with synchronization to the end of the measurement before reading out the result. This is only possible for
		single sweep mode. See also method RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Result')
			:return: modulation_depth: Modulation depth in %."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:MDEPth:RESult{trace_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'ResultCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResultCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
