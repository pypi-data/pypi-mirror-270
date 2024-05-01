from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class XCls:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def get(self, trace: enums.TraceTypeNumeric, window=repcap.Window.Default) -> str:
		"""SCPI: TRACe<n>[:DATA]:X \n
		Snippet: value: str = driver.applications.k18AmplifierEt.trace.data.x.get(trace = enums.TraceTypeNumeric.TRACe1, window = repcap.Window.Default) \n
		This command queries the horizontal trace data for each sweep point in the specified window, for example the frequency in
		frequency domain or the time in time domain measurements. This is especially useful for traces with non-equidistant
		x-values. \n
			:param trace: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
			:return: result: No help available"""
		param = Conversions.enum_scalar_to_str(trace, enums.TraceTypeNumeric)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'TRACe{window_cmd_val}:DATA:X? {param}')
		return trim_str_response(response)
