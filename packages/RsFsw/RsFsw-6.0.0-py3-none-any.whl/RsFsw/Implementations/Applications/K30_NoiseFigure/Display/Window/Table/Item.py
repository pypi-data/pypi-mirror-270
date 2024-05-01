from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ItemCls:
	"""Item commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("item", core, parent)

	def set(self, items: enums.NoiseFigureResult, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TABLe:ITEM \n
		Snippet: driver.applications.k30NoiseFigure.display.window.table.item.set(items = enums.NoiseFigureResult.CPCold, state = False, window = repcap.Window.Default) \n
		Defines which items are displayed in the 'Result Summary' (see 'Result Summary Detailed' and 'Result Summary Global') .
		Note that the results are always calculated, regardless of their visibility in the 'Result Summary'. \n
			:param items: No help available
			:param state: ON | OFF | 0 | 1 OFF | 0 Item is displayed in 'Result Summary'. ON | 1 Item is not displayed in 'Result Summary'.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('items', items, DataType.Enum, enums.NoiseFigureResult), ArgSingle('state', state, DataType.Boolean))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TABLe:ITEM {param}'.rstrip())

	# noinspection PyTypeChecker
	class ItemStruct(StructBase):
		"""Response structure. Fields: \n
			- Items: enums.NoiseFigureResult: No parameter help available
			- State: bool: ON | OFF | 0 | 1 OFF | 0 Item is displayed in 'Result Summary'. ON | 1 Item is not displayed in 'Result Summary'."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Items', enums.NoiseFigureResult),
			ArgStruct.scalar_bool('State')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Items: enums.NoiseFigureResult = None
			self.State: bool = None

	def get(self, window=repcap.Window.Default) -> ItemStruct:
		"""SCPI: DISPlay[:WINDow<n>]:TABLe:ITEM \n
		Snippet: value: ItemStruct = driver.applications.k30NoiseFigure.display.window.table.item.get(window = repcap.Window.Default) \n
		Defines which items are displayed in the 'Result Summary' (see 'Result Summary Detailed' and 'Result Summary Global') .
		Note that the results are always calculated, regardless of their visibility in the 'Result Summary'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: structure: for return value, see the help for ItemStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'DISPlay:WINDow{window_cmd_val}:TABLe:ITEM?', self.__class__.ItemStruct())
