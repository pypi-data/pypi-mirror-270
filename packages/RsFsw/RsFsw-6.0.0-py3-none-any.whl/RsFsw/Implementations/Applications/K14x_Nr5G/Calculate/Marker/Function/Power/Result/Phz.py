from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhzCls:
	"""Phz commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phz", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer:RESult:PHZ \n
		Snippet: driver.applications.k14Xnr5G.calculate.marker.function.power.result.phz.set(state = False, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Selects the unit the FSW returns results for power measurements. You can query results with method RsFsw.Calculate.Marker.
		Function.Power.Result.set. For LTE and 5G applications, use the command method RsFsw.Calculate.Marker.Function.Power.
		Result.Unit.set. \n
			:param state: ON | OFF | 1 | 0 ON | 1 Channel power density in dBm/Hz OFF | 0 Channel power in dBm
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer:RESult:PHZ {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> bool:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer:RESult:PHZ \n
		Snippet: value: bool = driver.applications.k14Xnr5G.calculate.marker.function.power.result.phz.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Selects the unit the FSW returns results for power measurements. You can query results with method RsFsw.Calculate.Marker.
		Function.Power.Result.set. For LTE and 5G applications, use the command method RsFsw.Calculate.Marker.Function.Power.
		Result.Unit.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: state: ON | OFF | 1 | 0 ON | 1 Channel power density in dBm/Hz OFF | 0 Channel power in dBm"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer:RESult:PHZ?')
		return Conversions.str_to_bool(response)
