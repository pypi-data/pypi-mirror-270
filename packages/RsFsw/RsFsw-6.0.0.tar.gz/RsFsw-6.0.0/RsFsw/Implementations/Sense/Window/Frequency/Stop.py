from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StopCls:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def set(self, stop: float, window=repcap.Window.Default) -> None:
		"""SCPI: [SENSe][:WINDow<n>]:FREQuency:STOP \n
		Snippet: driver.sense.window.frequency.stop.set(stop = 1.0, window = repcap.Window.Default) \n
		No command help available \n
			:param stop: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(stop)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:WINDow{window_cmd_val}:FREQuency:STOP {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: [SENSe][:WINDow<n>]:FREQuency:STOP \n
		Snippet: value: float = driver.sense.window.frequency.stop.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: stop: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:WINDow{window_cmd_val}:FREQuency:STOP?')
		return Conversions.str_to_float(response)
