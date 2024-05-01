from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, filterPy=repcap.FilterPy.Default) -> None:
		"""SCPI: [SENSe]:FILTer<n>:HPASs[:STATe] \n
		Snippet: driver.sense.filterPy.hpass.state.set(state = False, filterPy = repcap.FilterPy.Default) \n
		Activates/deactivates the selected high pass filter for the specified evaluation. For details on the high pass filter,
		refer to 'High Pass'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
		"""
		param = Conversions.bool_to_str(state)
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		self._core.io.write(f'SENSe:FILTer{filterPy_cmd_val}:HPASs:STATe {param}')

	def get(self, filterPy=repcap.FilterPy.Default) -> bool:
		"""SCPI: [SENSe]:FILTer<n>:HPASs[:STATe] \n
		Snippet: value: bool = driver.sense.filterPy.hpass.state.get(filterPy = repcap.FilterPy.Default) \n
		Activates/deactivates the selected high pass filter for the specified evaluation. For details on the high pass filter,
		refer to 'High Pass'. \n
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		response = self._core.io.query_str(f'SENSe:FILTer{filterPy_cmd_val}:HPASs:STATe?')
		return Conversions.str_to_bool(response)
