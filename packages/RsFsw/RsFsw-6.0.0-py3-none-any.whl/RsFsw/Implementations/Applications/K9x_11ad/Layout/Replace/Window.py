from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WindowCls:
	"""Window commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("window", core, parent)

	def set(self, window_name: str, window_type: enums.WindowTypeK9X) -> None:
		"""SCPI: LAYout:REPLace[:WINDow] \n
		Snippet: driver.applications.k9X11Ad.layout.replace.window.set(window_name = 'abc', window_type = enums.WindowTypeK9X.ChannelFreqResponse=CFR) \n
		Replaces the window type (for example from 'Diagram' to 'Result Summary') of an already existing window in the active
		channel while keeping its position, index and window name. To add a new window, use the method RsFsw.Layout.Add.Window.
		get_ command. \n
			:param window_name: String containing the name of the existing window. By default, the name of a window is the same as its index. To determine the name and index of all active windows in the active channel, use the method RsFsw.Layout.Catalog.Window.get_ query.
			:param window_type: (enum or string) Type of result display you want to use in the existing window. See method RsFsw.Layout.Add.Window.get_ for a list of available window types.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('window_name', window_name, DataType.String), ArgSingle('window_type', window_type, DataType.EnumExt, enums.WindowTypeK9X))
		self._core.io.write_with_opc(f'LAYout:REPLace:WINDow {param}'.rstrip())
