from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WlanCls:
	"""Wlan commands group definition. 51 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wlan", core, parent)

	@property
	def mimo(self):
		"""mimo commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import MimoCls
			self._mimo = MimoCls(self._core, self._cmd_group)
		return self._mimo

	@property
	def dutConfig(self):
		"""dutConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dutConfig'):
			from .DutConfig import DutConfigCls
			self._dutConfig = DutConfigCls(self._core, self._cmd_group)
		return self._dutConfig

	@property
	def antMatrix(self):
		"""antMatrix commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_antMatrix'):
			from .AntMatrix import AntMatrixCls
			self._antMatrix = AntMatrixCls(self._core, self._cmd_group)
		return self._antMatrix

	@property
	def gtime(self):
		"""gtime commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gtime'):
			from .Gtime import GtimeCls
			self._gtime = GtimeCls(self._core, self._cmd_group)
		return self._gtime

	@property
	def ruConfig(self):
		"""ruConfig commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_ruConfig'):
			from .RuConfig import RuConfigCls
			self._ruConfig = RuConfigCls(self._core, self._cmd_group)
		return self._ruConfig

	@property
	def rsync(self):
		"""rsync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rsync'):
			from .Rsync import RsyncCls
			self._rsync = RsyncCls(self._core, self._cmd_group)
		return self._rsync

	@property
	def sspacing(self):
		"""sspacing commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_sspacing'):
			from .Sspacing import SspacingCls
			self._sspacing = SspacingCls(self._core, self._cmd_group)
		return self._sspacing

	@property
	def stbc(self):
		"""stbc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_stbc'):
			from .Stbc import StbcCls
			self._stbc = StbcCls(self._core, self._cmd_group)
		return self._stbc

	@property
	def extension(self):
		"""extension commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_extension'):
			from .Extension import ExtensionCls
			self._extension = ExtensionCls(self._core, self._cmd_group)
		return self._extension

	@property
	def smapping(self):
		"""smapping commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_smapping'):
			from .Smapping import SmappingCls
			self._smapping = SmappingCls(self._core, self._cmd_group)
		return self._smapping

	@property
	def payload(self):
		"""payload commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_payload'):
			from .Payload import PayloadCls
			self._payload = PayloadCls(self._core, self._cmd_group)
		return self._payload

	@property
	def pvError(self):
		"""pvError commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pvError'):
			from .PvError import PvErrorCls
			self._pvError = PvErrorCls(self._core, self._cmd_group)
		return self._pvError

	def clone(self) -> 'WlanCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = WlanCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
