from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SizeCls:
	"""Size commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("size", core, parent)

	def set(self, size: enums.Size, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:SIZE \n
		Snippet: driver.applications.k14Xnr5G.display.window.subwindow.size.set(size = enums.Size.LARGe, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		Maximizes the size of the selected result display subwindow temporarily. To change the size of several windows on the
		screen permanently, use the method RsFsw.Applications.K17_Mcgd.Layout.Splitter.set command (see method RsFsw.Applications.
		K17_Mcgd.Layout.Splitter.set) . \n
			:param size: FULL | SPLit FULL Maximizes the selected subwindow to full screen. Other windows are still active in the background. SPLit Reduces the size of the selected subwindow to its original size. If more than one measurement window was displayed originally, these are visible again.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
		"""
		param = Conversions.enum_scalar_to_str(size, enums.Size)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:SIZE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default) -> enums.Size:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:SIZE \n
		Snippet: value: enums.Size = driver.applications.k14Xnr5G.display.window.subwindow.size.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		Maximizes the size of the selected result display subwindow temporarily. To change the size of several windows on the
		screen permanently, use the method RsFsw.Applications.K17_Mcgd.Layout.Splitter.set command (see method RsFsw.Applications.
		K17_Mcgd.Layout.Splitter.set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:return: size: FULL | SPLit FULL Maximizes the selected subwindow to full screen. Other windows are still active in the background. SPLit Reduces the size of the selected subwindow to its original size. If more than one measurement window was displayed originally, these are visible again."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:SIZE?')
		return Conversions.str_to_scalar_enum(response, enums.Size)
