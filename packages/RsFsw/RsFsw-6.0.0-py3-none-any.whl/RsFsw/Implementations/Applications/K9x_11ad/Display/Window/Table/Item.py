from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
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

	def set(self, item: enums.TableItemK9X, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TABLe:ITEM \n
		Snippet: driver.applications.k9X11Ad.display.window.table.item.set(item = enums.TableItemK9X.RxAll_CenterFreqError=RCFerror, state = False, window = repcap.Window.Default) \n
		Defines which items are displayed in the 'Result Summary' (see 'Result Summary Detailed' and 'Result Summary Global') .
		Note that the results are always calculated, regardless of their visibility in the 'Result Summary'. \n
			:param item: Item to be included in 'Result Summary'. For an overview of possible results and the required parameters see the tables below.
			:param state: ON | OFF | 0 | 1 OFF | 0 Item is displayed in 'Result Summary'. ON | 1 Item is not displayed in 'Result Summary'.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('item', item, DataType.Enum, enums.TableItemK9X), ArgSingle('state', state, DataType.Boolean))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write_with_opc(f'DISPlay:WINDow{window_cmd_val}:TABLe:ITEM {param}'.rstrip())
