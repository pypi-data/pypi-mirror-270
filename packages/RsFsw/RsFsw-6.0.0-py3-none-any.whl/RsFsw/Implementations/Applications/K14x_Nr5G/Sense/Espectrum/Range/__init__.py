from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RangeCls:
	"""Range commands group definition. 29 total commands, 12 Subgroups, 1 group commands
	Repeated Capability: RangePy, default value after init: RangePy.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_rangePy_get', 'repcap_rangePy_set', repcap.RangePy.Ix1)

	def repcap_rangePy_set(self, rangePy: repcap.RangePy) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RangePy.Default
		Default value after init: RangePy.Ix1"""
		self._cmd_group.set_repcap_enum_value(rangePy)

	def repcap_rangePy_get(self) -> repcap.RangePy:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bandwidth(self):
		"""bandwidth commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import CountCls
			self._count = CountCls(self._core, self._cmd_group)
		return self._count

	@property
	def filterPy(self):
		"""filterPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	@property
	def frequency(self):
		"""frequency commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def inputPy(self):
		"""inputPy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPyCls
			self._inputPy = InputPyCls(self._core, self._cmd_group)
		return self._inputPy

	@property
	def insert(self):
		"""insert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_insert'):
			from .Insert import InsertCls
			self._insert = InsertCls(self._core, self._cmd_group)
		return self._insert

	@property
	def limit(self):
		"""limit commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	@property
	def mlCalc(self):
		"""mlCalc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mlCalc'):
			from .MlCalc import MlCalcCls
			self._mlCalc = MlCalcCls(self._core, self._cmd_group)
		return self._mlCalc

	@property
	def points(self):
		"""points commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_points'):
			from .Points import PointsCls
			self._points = PointsCls(self._core, self._cmd_group)
		return self._points

	@property
	def refLevel(self):
		"""refLevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_refLevel'):
			from .RefLevel import RefLevelCls
			self._refLevel = RefLevelCls(self._core, self._cmd_group)
		return self._refLevel

	@property
	def sweep(self):
		"""sweep commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import SweepCls
			self._sweep = SweepCls(self._core, self._cmd_group)
		return self._sweep

	@property
	def transducer(self):
		"""transducer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_transducer'):
			from .Transducer import TransducerCls
			self._transducer = TransducerCls(self._core, self._cmd_group)
		return self._transducer

	def delete(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<range>:DELete \n
		Snippet: driver.applications.k14Xnr5G.sense.espectrum.range.delete(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		Removes a range from the sweep list. Note that
			INTRO_CMD_HELP: Prerequisites for this command \n
			- you cannot delete the reference range
			- a minimum of three ranges is mandatory. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:DELete')

	def delete_with_opc(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default, opc_timeout_ms: int = -1) -> None:
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<range>:DELete \n
		Snippet: driver.applications.k14Xnr5G.sense.espectrum.range.delete_with_opc(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		Removes a range from the sweep list. Note that
			INTRO_CMD_HELP: Prerequisites for this command \n
			- you cannot delete the reference range
			- a minimum of three ranges is mandatory. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:DELete', opc_timeout_ms)

	def clone(self) -> 'RangeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RangeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
