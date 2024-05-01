from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.Utilities import trim_str_response
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WindowCls:
	"""Window commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("window", core, parent)

	def get(self, window_name: str, direction: enums.WindowDirection, window_type: enums.WindowTypeK149) -> str:
		"""SCPI: LAYout:ADD[:WINDow] \n
		Snippet: value: str = driver.applications.k149Uwb.layout.add.window.get(window_name = 'abc', direction = enums.WindowDirection.ABOVe, window_type = enums.WindowTypeK149.ChipPhaseJitter=CJPH) \n
		Adds a window to the display in the active channel. Is always used as a query so that you immediately obtain the name of
		the new window as a result. To replace an existing window, use the method RsFsw.Layout.Replace.Window.set command. \n
			:param window_name: String containing the name of the existing window the new window is inserted next to. By default, the name of a window is the same as its index. To determine the name and index of all active windows, use the method RsFsw.Layout.Catalog.Window.get_ query.
			:param direction: LEFT | RIGHt | ABOVe | BELow Direction the new window is added relative to the existing window.
			:param window_type: (enum or string) text value Type of result display (evaluation method) you want to add. See the table below for available parameter values.
			:return: new_window_name: When adding a new window, the command returns its name (by default the same as its number) as a result."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('window_name', window_name, DataType.String), ArgSingle('direction', direction, DataType.Enum, enums.WindowDirection), ArgSingle('window_type', window_type, DataType.EnumExt, enums.WindowTypeK149))
		response = self._core.io.query_str_with_opc(f'LAYout:ADD:WINDow? {param}'.rstrip())
		return trim_str_response(response)
