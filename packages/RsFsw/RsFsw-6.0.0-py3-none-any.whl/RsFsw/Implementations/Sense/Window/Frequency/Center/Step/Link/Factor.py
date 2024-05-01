from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FactorCls:
	"""Factor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("factor", core, parent)

	def set(self, link_factor: float, window=repcap.Window.Default) -> None:
		"""SCPI: [SENSe][:WINDow<n>]:FREQuency:CENTer:STEP:LINK:FACTor \n
		Snippet: driver.sense.window.frequency.center.step.link.factor.set(link_factor = 1.0, window = repcap.Window.Default) \n
		No command help available \n
			:param link_factor: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(link_factor)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:WINDow{window_cmd_val}:FREQuency:CENTer:STEP:LINK:FACTor {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: [SENSe][:WINDow<n>]:FREQuency:CENTer:STEP:LINK:FACTor \n
		Snippet: value: float = driver.sense.window.frequency.center.step.link.factor.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: link_factor: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:WINDow{window_cmd_val}:FREQuency:CENTer:STEP:LINK:FACTor?')
		return Conversions.str_to_float(response)
