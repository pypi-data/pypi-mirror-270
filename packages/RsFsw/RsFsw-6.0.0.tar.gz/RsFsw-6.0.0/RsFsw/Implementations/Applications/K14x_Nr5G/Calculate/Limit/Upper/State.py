from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:UPPer:STATe \n
		Snippet: driver.applications.k14Xnr5G.calculate.limit.upper.state.set(state = False, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Turns an upper limit line on and off. Before you can use the command, you have to select a limit line with method RsFsw.
		Calculate.Limit.Name.set. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:UPPer:STATe {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> bool:
		"""SCPI: CALCulate<n>:LIMit<li>:UPPer:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.calculate.limit.upper.state.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Turns an upper limit line on and off. Before you can use the command, you have to select a limit line with method RsFsw.
		Calculate.Limit.Name.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:UPPer:STATe?')
		return Conversions.str_to_bool(response)
