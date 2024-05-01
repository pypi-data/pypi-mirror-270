from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def get(self, trace_type: enums.TraceTypeDdem, window=repcap.Window.Default) -> List[float]:
		"""SCPI: TRACe<n>[:DATA] \n
		Snippet: value: List[float] = driver.applications.k70Vsa.trace.data.get(trace_type = enums.TraceTypeDdem.MSTRace, window = repcap.Window.Default) \n
		This command queries current trace data and measurement results. In the Spectrum application only, you can use it as a
		setting command to transfer trace data from an external source to the FSW. The data format depends on method RsFsw.
		FormatPy.Data.set. \n
			:param trace_type: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
			:return: trace_ydata: No help available"""
		param = Conversions.enum_scalar_to_str(trace_type, enums.TraceTypeDdem)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_bin_or_ascii_float_list(f'FORMAT REAL,32;TRACe{window_cmd_val}:DATA? {param}')
		return response
