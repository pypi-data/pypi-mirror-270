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

	def set(self, source_window: str, target_window: str, direction: enums.WindowDirReplace) -> None:
		"""SCPI: LAYout:MOVE[:WINDow] \n
		Snippet: driver.applications.k30NoiseFigure.layout.move.window.set(source_window = 'abc', target_window = 'abc', direction = enums.WindowDirReplace.ABOVe) \n
		No command help available \n
			:param source_window: LEFT | RIGHt | ABOVe | BELow | REPLace Destination the selected window is moved to, relative to the reference window.
			:param target_window: LEFT | RIGHt | ABOVe | BELow | REPLace Destination the selected window is moved to, relative to the reference window.
			:param direction: LEFT | RIGHt | ABOVe | BELow | REPLace Destination the selected window is moved to, relative to the reference window.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('source_window', source_window, DataType.String), ArgSingle('target_window', target_window, DataType.String), ArgSingle('direction', direction, DataType.Enum, enums.WindowDirReplace))
		self._core.io.write_with_opc(f'LAYout:MOVE:WINDow {param}'.rstrip())
