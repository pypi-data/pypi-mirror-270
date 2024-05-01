from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BwPartCls:
	"""BwPart commands group definition. 128 total commands, 13 Subgroups, 1 group commands
	Repeated Capability: BwPart, default value after init: BwPart.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bwPart", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_bwPart_get', 'repcap_bwPart_set', repcap.BwPart.Nr1)

	def repcap_bwPart_set(self, bwPart: repcap.BwPart) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BwPart.Default
		Default value after init: BwPart.Nr1"""
		self._cmd_group.set_repcap_enum_value(bwPart)

	def repcap_bwPart_get(self) -> repcap.BwPart:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Add import AddCls
			self._add = AddCls(self._core, self._cmd_group)
		return self._add

	@property
	def csi(self):
		"""csi commands group. 15 Sub-classes, 0 commands."""
		if not hasattr(self, '_csi'):
			from .Csi import CsiCls
			self._csi = CsiCls(self._core, self._cmd_group)
		return self._csi

	@property
	def prs(self):
		"""prs commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_prs'):
			from .Prs import PrsCls
			self._prs = PrsCls(self._core, self._cmd_group)
		return self._prs

	@property
	def cslot(self):
		"""cslot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cslot'):
			from .Cslot import CslotCls
			self._cslot = CslotCls(self._core, self._cmd_group)
		return self._cslot

	@property
	def detection(self):
		"""detection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_detection'):
			from .Detection import DetectionCls
			self._detection = DetectionCls(self._core, self._cmd_group)
		return self._detection

	@property
	def duplicate(self):
		"""duplicate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duplicate'):
			from .Duplicate import DuplicateCls
			self._duplicate = DuplicateCls(self._core, self._cmd_group)
		return self._duplicate

	@property
	def prb(self):
		"""prb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prb'):
			from .Prb import PrbCls
			self._prb = PrbCls(self._core, self._cmd_group)
		return self._prb

	@property
	def rbCount(self):
		"""rbCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbCount'):
			from .RbCount import RbCountCls
			self._rbCount = RbCountCls(self._core, self._cmd_group)
		return self._rbCount

	@property
	def rbOffset(self):
		"""rbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbOffset'):
			from .RbOffset import RbOffsetCls
			self._rbOffset = RbOffsetCls(self._core, self._cmd_group)
		return self._rbOffset

	@property
	def remove(self):
		"""remove commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_remove'):
			from .Remove import RemoveCls
			self._remove = RemoveCls(self._core, self._cmd_group)
		return self._remove

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import ScountCls
			self._scount = ScountCls(self._core, self._cmd_group)
		return self._scount

	@property
	def slot(self):
		"""slot commands group. 9 Sub-classes, 2 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import SlotCls
			self._slot = SlotCls(self._core, self._cmd_group)
		return self._slot

	@property
	def sspacing(self):
		"""sspacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sspacing'):
			from .Sspacing import SspacingCls
			self._sspacing = SspacingCls(self._core, self._cmd_group)
		return self._sspacing

	def clear(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:CLEar \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.clear(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default) \n
		Deletes all bandwidth parts. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
		"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:CLEar')

	def clear_with_opc(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, opc_timeout_ms: int = -1) -> None:
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:CLEar \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.clear_with_opc(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default) \n
		Deletes all bandwidth parts. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:CLEar', opc_timeout_ms)

	def clone(self) -> 'BwPartCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BwPartCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
