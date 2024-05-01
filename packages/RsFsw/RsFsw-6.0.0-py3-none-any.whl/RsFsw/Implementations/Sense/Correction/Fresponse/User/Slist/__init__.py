from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SlistCls:
	"""Slist commands group definition. 13 total commands, 8 Subgroups, 2 group commands
	Repeated Capability: TouchStone, default value after init: TouchStone.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slist", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_touchStone_get', 'repcap_touchStone_set', repcap.TouchStone.Ix1)

	def repcap_touchStone_set(self, touchStone: repcap.TouchStone) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TouchStone.Default
		Default value after init: TouchStone.Ix1"""
		self._cmd_group.set_repcap_enum_value(touchStone)

	def repcap_touchStone_get(self) -> repcap.TouchStone:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def size(self):
		"""size commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_size'):
			from .Size import SizeCls
			self._size = SizeCls(self._core, self._cmd_group)
		return self._size

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	@property
	def remove(self):
		"""remove commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_remove'):
			from .Remove import RemoveCls
			self._remove = RemoveCls(self._core, self._cmd_group)
		return self._remove

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import SelectCls
			self._select = SelectCls(self._core, self._cmd_group)
		return self._select

	@property
	def insert(self):
		"""insert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_insert'):
			from .Insert import InsertCls
			self._insert = InsertCls(self._core, self._cmd_group)
		return self._insert

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def ports(self):
		"""ports commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ports'):
			from .Ports import PortsCls
			self._ports = PortsCls(self._core, self._cmd_group)
		return self._ports

	@property
	def data(self):
		"""data commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_data'):
			from .Data import DataCls
			self._data = DataCls(self._core, self._cmd_group)
		return self._data

	def clear(self, touchStone=repcap.TouchStone.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:SLISt<sli>:CLEar \n
		Snippet: driver.sense.correction.fresponse.user.slist.clear(touchStone = repcap.TouchStone.Default) \n
		Removes all touchstone files from the current configuration for the selected or all input types. \n
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
		"""
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		self._core.io.write(f'SENSe:CORRection:FRESponse:USER:SLISt{touchStone_cmd_val}:CLEar')

	def clear_with_opc(self, touchStone=repcap.TouchStone.Default, opc_timeout_ms: int = -1) -> None:
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:SLISt<sli>:CLEar \n
		Snippet: driver.sense.correction.fresponse.user.slist.clear_with_opc(touchStone = repcap.TouchStone.Default) \n
		Removes all touchstone files from the current configuration for the selected or all input types. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:CORRection:FRESponse:USER:SLISt{touchStone_cmd_val}:CLEar', opc_timeout_ms)

	def move(self, direction: enums.UpDownDirection, touchStone=repcap.TouchStone.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:SLISt<sli>:MOVE \n
		Snippet: driver.sense.correction.fresponse.user.slist.move(direction = enums.UpDownDirection.DOWN, touchStone = repcap.TouchStone.Default) \n
		Moves the selected Touchstone file one position up or down in the list of files, changing the order in which the
		correction data is applied. \n
			:param direction: UP | DOWN
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
		"""
		param = Conversions.enum_scalar_to_str(direction, enums.UpDownDirection)
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		self._core.io.write(f'SENSe:CORRection:FRESponse:USER:SLISt{touchStone_cmd_val}:MOVE {param}')

	def clone(self) -> 'SlistCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SlistCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
