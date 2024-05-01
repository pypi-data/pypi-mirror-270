from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WindowCls:
	"""Window commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("window", core, parent)

	def set(self, name: str) -> None:
		"""SCPI: LAYout:REMove[:WINDow] \n
		Snippet: driver.applications.k70Vsa.layout.remove.window.set(name = 'abc') \n
		Removes a window from the display in the active channel. \n
			:param name: String containing the name of the window. In the default state, the name of the window is its index.
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write_with_opc(f'LAYout:REMove:WINDow {param}')
