from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ItemCls:
	"""Item commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("item", core, parent)

	@property
	def maccuracy(self):
		"""maccuracy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_maccuracy'):
			from .Maccuracy import MaccuracyCls
			self._maccuracy = MaccuracyCls(self._core, self._cmd_group)
		return self._maccuracy

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def vcurrent(self):
		"""vcurrent commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_vcurrent'):
			from .Vcurrent import VcurrentCls
			self._vcurrent = VcurrentCls(self._core, self._cmd_group)
		return self._vcurrent

	def set(self, item: enums.TableItem, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TABLe:ITEM \n
		Snippet: driver.applications.k18AmplifierEt.display.window.table.item.set(item = enums.TableItem.ADRoop, state = False, window = repcap.Window.Default) \n
		Defines which items are displayed in the 'Result Summary' (see 'Result Summary Detailed' and 'Result Summary Global') .
		Note that the results are always calculated, regardless of their visibility in the 'Result Summary'. \n
			:param item: Item to be included in 'Result Summary'. For an overview of possible results and the required parameters see the tables below.
			:param state: ON | OFF | 0 | 1 OFF | 0 Item is displayed in 'Result Summary'. ON | 1 Item is not displayed in 'Result Summary'.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('item', item, DataType.Enum, enums.TableItem), ArgSingle('state', state, DataType.Boolean))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TABLe:ITEM {param}'.rstrip())

	def get(self, item: enums.TableItem, window=repcap.Window.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:TABLe:ITEM \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.display.window.table.item.get(item = enums.TableItem.ADRoop, window = repcap.Window.Default) \n
		Defines which items are displayed in the 'Result Summary' (see 'Result Summary Detailed' and 'Result Summary Global') .
		Note that the results are always calculated, regardless of their visibility in the 'Result Summary'. \n
			:param item: Item to be included in 'Result Summary'. For an overview of possible results and the required parameters see the tables below.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Item is displayed in 'Result Summary'. ON | 1 Item is not displayed in 'Result Summary'."""
		param = Conversions.enum_scalar_to_str(item, enums.TableItem)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TABLe:ITEM? {param}')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'ItemCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ItemCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
