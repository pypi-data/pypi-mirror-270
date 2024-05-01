from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefPositionCls:
	"""RefPosition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refPosition", core, parent)

	def set(self, rpos: float, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:X[:SCALe]:RPOSition \n
		Snippet: driver.applications.k70Vsa.display.window.trace.x.scale.refPosition.set(rpos = 1.0, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Defines the position of the reference value for the X axis. Setting the position of the reference value is possible only
		for statistical result displays. All other result displays support the query only. \n
			:param rpos: numeric_value Unit: PCT
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.decimal_value_to_str(rpos)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:X:SCALe:RPOSition {param}')

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:X[:SCALe]:RPOSition \n
		Snippet: value: float = driver.applications.k70Vsa.display.window.trace.x.scale.refPosition.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Defines the position of the reference value for the X axis. Setting the position of the reference value is possible only
		for statistical result displays. All other result displays support the query only. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: rpos: numeric_value Unit: PCT"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:X:SCALe:RPOSition?')
		return Conversions.str_to_float(response)
