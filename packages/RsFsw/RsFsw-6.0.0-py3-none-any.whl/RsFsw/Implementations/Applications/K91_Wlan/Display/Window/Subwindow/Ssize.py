from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SsizeCls:
	"""Ssize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssize", core, parent)

	def set(self, size: enums.SubwindowSize, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:SSIZe \n
		Snippet: driver.applications.k91Wlan.display.window.subwindow.ssize.set(size = enums.SubwindowSize.FULL, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		No command help available \n
			:param size: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
		"""
		param = Conversions.enum_scalar_to_str(size, enums.SubwindowSize)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:SSIZe {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default) -> enums.SubwindowSize:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:SSIZe \n
		Snippet: value: enums.SubwindowSize = driver.applications.k91Wlan.display.window.subwindow.ssize.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:return: size: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:SSIZe?')
		return Conversions.str_to_scalar_enum(response, enums.SubwindowSize)
