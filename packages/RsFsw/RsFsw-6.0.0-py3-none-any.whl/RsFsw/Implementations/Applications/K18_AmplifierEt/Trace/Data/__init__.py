from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def x(self):
		"""x commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_x'):
			from .X import XCls
			self._x = XCls(self._core, self._cmd_group)
		return self._x

	def get(self, trace: enums.TraceTypeNumeric, window=repcap.Window.Default) -> str:
		"""SCPI: TRACe<n>[:DATA] \n
		Snippet: value: str = driver.applications.k18AmplifierEt.trace.data.get(trace = enums.TraceTypeNumeric.TRACe1, window = repcap.Window.Default) \n
		This command queries current trace data and measurement results. In the Spectrum application only, you can use it as a
		setting command to transfer trace data from an external source to the FSW. The data format depends on method RsFsw.
		FormatPy.Data.set. \n
			:param trace: TRACE1 | TRACE2 | TRACE3 | TRACE4 | TRACE5 | TRACE6 Selects the trace to write the data to (Spectrum application only) .
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
			:return: result: No help available"""
		param = Conversions.enum_scalar_to_str(trace, enums.TraceTypeNumeric)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'TRACe{window_cmd_val}:DATA? {param}')
		return trim_str_response(response)

	def clone(self) -> 'DataCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DataCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
