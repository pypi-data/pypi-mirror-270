from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit:MACCuracy:FERRor:PCURrent:STATe \n
		Snippet: driver.applications.k70Vsa.calculate.limit.maccuracy.freqError.pcurrent.state.set(state = False, window = repcap.Window.Default) \n
		Switches the limit check for the selected result type and limit type on or off. \n
			:param state: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit:MACCuracy:FERRor:PCURrent:STATe {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:LIMit:MACCuracy:FERRor:PCURrent:STATe \n
		Snippet: value: bool = driver.applications.k70Vsa.calculate.limit.maccuracy.freqError.pcurrent.state.get(window = repcap.Window.Default) \n
		Switches the limit check for the selected result type and limit type on or off. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit:MACCuracy:FERRor:PCURrent:STATe?')
		return Conversions.str_to_bool(response)
