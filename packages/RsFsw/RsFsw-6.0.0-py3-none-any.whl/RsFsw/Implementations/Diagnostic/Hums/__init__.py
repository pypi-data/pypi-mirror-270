from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HumsCls:
	"""Hums commands group definition. 25 total commands, 13 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hums", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def utilization(self):
		"""utilization commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_utilization'):
			from .Utilization import UtilizationCls
			self._utilization = UtilizationCls(self._core, self._cmd_group)
		return self._utilization

	@property
	def bios(self):
		"""bios commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bios'):
			from .Bios import BiosCls
			self._bios = BiosCls(self._core, self._cmd_group)
		return self._bios

	@property
	def device(self):
		"""device commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_device'):
			from .Device import DeviceCls
			self._device = DeviceCls(self._core, self._cmd_group)
		return self._device

	@property
	def equipment(self):
		"""equipment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_equipment'):
			from .Equipment import EquipmentCls
			self._equipment = EquipmentCls(self._core, self._cmd_group)
		return self._equipment

	@property
	def sw(self):
		"""sw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sw'):
			from .Sw import SwCls
			self._sw = SwCls(self._core, self._cmd_group)
		return self._sw

	@property
	def storage(self):
		"""storage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_storage'):
			from .Storage import StorageCls
			self._storage = StorageCls(self._core, self._cmd_group)
		return self._storage

	@property
	def system(self):
		"""system commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_system'):
			from .System import SystemCls
			self._system = SystemCls(self._core, self._cmd_group)
		return self._system

	@property
	def security(self):
		"""security commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_security'):
			from .Security import SecurityCls
			self._security = SecurityCls(self._core, self._cmd_group)
		return self._security

	@property
	def service(self):
		"""service commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_service'):
			from .Service import ServiceCls
			self._service = ServiceCls(self._core, self._cmd_group)
		return self._service

	@property
	def tags(self):
		"""tags commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_tags'):
			from .Tags import TagsCls
			self._tags = TagsCls(self._core, self._cmd_group)
		return self._tags

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPyCls
			self._formatPy = FormatPyCls(self._core, self._cmd_group)
		return self._formatPy

	def delete_all(self) -> None:
		"""SCPI: DIAGnostic:HUMS:DELete:ALL \n
		Snippet: driver.diagnostic.hums.delete_all() \n
		Deletes the complete HUMS data. This includes device history, device tags, SCPI connections, utilization history and
		utilizations. \n
		"""
		self._core.io.write(f'DIAGnostic:HUMS:DELete:ALL')

	def delete_all_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: DIAGnostic:HUMS:DELete:ALL \n
		Snippet: driver.diagnostic.hums.delete_all_with_opc() \n
		Deletes the complete HUMS data. This includes device history, device tags, SCPI connections, utilization history and
		utilizations. \n
		Same as delete_all, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DIAGnostic:HUMS:DELete:ALL', opc_timeout_ms)

	def save(self, path: str) -> None:
		"""SCPI: DIAGnostic:HUMS:SAVE \n
		Snippet: driver.diagnostic.hums.save(path = 'abc') \n
		No command help available \n
			:param path: No help available
		"""
		param = Conversions.value_to_quoted_str(path)
		self._core.io.write(f'DIAGnostic:HUMS:SAVE {param}')

	def clone(self) -> 'HumsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HumsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
