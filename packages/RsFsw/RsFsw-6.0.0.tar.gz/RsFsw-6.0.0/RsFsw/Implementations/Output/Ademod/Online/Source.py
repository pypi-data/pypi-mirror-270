from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SourceCls:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, window_name: enums.WindowName) -> None:
		"""SCPI: OUTPut:ADEMod[:ONLine]:SOURce \n
		Snippet: driver.output.ademod.online.source.set(window_name = enums.WindowName.FOCus) \n
		Selects the result display whose results are output. Only active time domain results can be selected. \n
			:param window_name: (enum or string) string String containing the name of the window. By default, the name of a window is the same as its index. To determine the name and index of all active windows, use the method RsFsw.Layout.Catalog.Window.get_ query. FOCus Dynamically switches to the currently selected window. If a window is selected that does not contain a time-domain result display, the selection is ignored and the previous setting is maintained.
		"""
		param = Conversions.enum_ext_scalar_to_str(window_name, enums.WindowName)
		self._core.io.write(f'OUTPut:ADEMod:ONLine:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.WindowName:
		"""SCPI: OUTPut:ADEMod[:ONLine]:SOURce \n
		Snippet: value: enums.WindowName = driver.output.ademod.online.source.get() \n
		Selects the result display whose results are output. Only active time domain results can be selected. \n
			:return: window_name: (enum or string) string String containing the name of the window. By default, the name of a window is the same as its index. To determine the name and index of all active windows, use the method RsFsw.Layout.Catalog.Window.get_ query. FOCus Dynamically switches to the currently selected window. If a window is selected that does not contain a time-domain result display, the selection is ignored and the previous setting is maintained."""
		response = self._core.io.query_str(f'OUTPut:ADEMod:ONLine:SOURce?')
		return Conversions.str_to_scalar_enum_ext(response, enums.WindowName)
