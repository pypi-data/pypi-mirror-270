from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SummaryCls:
	"""Summary commands group definition. 142 total commands, 33 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("summary", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def aapFail(self):
		"""aapFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aapFail'):
			from .AapFail import AapFailCls
			self._aapFail = AapFailCls(self._core, self._cmd_group)
		return self._aapFail

	@property
	def apFail(self):
		"""apFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apFail'):
			from .ApFail import ApFailCls
			self._apFail = ApFailCls(self._core, self._cmd_group)
		return self._apFail

	@property
	def arpFail(self):
		"""arpFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_arpFail'):
			from .ArpFail import ArpFailCls
			self._arpFail = ArpFailCls(self._core, self._cmd_group)
		return self._arpFail

	@property
	def bler(self):
		"""bler commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_bler'):
			from .Bler import BlerCls
			self._bler = BlerCls(self._core, self._cmd_group)
		return self._bler

	@property
	def eaaccs(self):
		"""eaaccs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eaaccs'):
			from .Eaaccs import EaaccsCls
			self._eaaccs = EaaccsCls(self._core, self._cmd_group)
		return self._eaaccs

	@property
	def evm(self):
		"""evm commands group. 28 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import EvmCls
			self._evm = EvmCls(self._core, self._cmd_group)
		return self._evm

	@property
	def freqError(self):
		"""freqError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqErrorCls
			self._freqError = FreqErrorCls(self._core, self._cmd_group)
		return self._freqError

	@property
	def foffset(self):
		"""foffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_foffset'):
			from .Foffset import FoffsetCls
			self._foffset = FoffsetCls(self._core, self._cmd_group)
		return self._foffset

	@property
	def gimbalance(self):
		"""gimbalance commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_gimbalance'):
			from .Gimbalance import GimbalanceCls
			self._gimbalance = GimbalanceCls(self._core, self._cmd_group)
		return self._gimbalance

	@property
	def iqOffset(self):
		"""iqOffset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def ostp(self):
		"""ostp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ostp'):
			from .Ostp import OstpCls
			self._ostp = OstpCls(self._core, self._cmd_group)
		return self._ostp

	@property
	def paccs(self):
		"""paccs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_paccs'):
			from .Paccs import PaccsCls
			self._paccs = PaccsCls(self._core, self._cmd_group)
		return self._paccs

	@property
	def power(self):
		"""power commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def quadError(self):
		"""quadError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_quadError'):
			from .QuadError import QuadErrorCls
			self._quadError = QuadErrorCls(self._core, self._cmd_group)
		return self._quadError

	@property
	def rsrp(self):
		"""rsrp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rsrp'):
			from .Rsrp import RsrpCls
			self._rsrp = RsrpCls(self._core, self._cmd_group)
		return self._rsrp

	@property
	def rstp(self):
		"""rstp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rstp'):
			from .Rstp import RstpCls
			self._rstp = RstpCls(self._core, self._cmd_group)
		return self._rstp

	@property
	def serror(self):
		"""serror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_serror'):
			from .Serror import SerrorCls
			self._serror = SerrorCls(self._core, self._cmd_group)
		return self._serror

	@property
	def capFail(self):
		"""capFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_capFail'):
			from .CapFail import CapFailCls
			self._capFail = CapFailCls(self._core, self._cmd_group)
		return self._capFail

	@property
	def cfrequency(self):
		"""cfrequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cfrequency'):
			from .Cfrequency import CfrequencyCls
			self._cfrequency = CfrequencyCls(self._core, self._cmd_group)
		return self._cfrequency

	@property
	def cpFail(self):
		"""cpFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cpFail'):
			from .CpFail import CpFailCls
			self._cpFail = CpFailCls(self._core, self._cmd_group)
		return self._cpFail

	@property
	def crpFail(self):
		"""crpFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crpFail'):
			from .CrpFail import CrpFailCls
			self._crpFail = CrpFailCls(self._core, self._cmd_group)
		return self._crpFail

	@property
	def crest(self):
		"""crest commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_crest'):
			from .Crest import CrestCls
			self._crest = CrestCls(self._core, self._cmd_group)
		return self._crest

	@property
	def mapFail(self):
		"""mapFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mapFail'):
			from .MapFail import MapFailCls
			self._mapFail = MapFailCls(self._core, self._cmd_group)
		return self._mapFail

	@property
	def mcpFail(self):
		"""mcpFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcpFail'):
			from .McpFail import McpFailCls
			self._mcpFail = McpFailCls(self._core, self._cmd_group)
		return self._mcpFail

	@property
	def mrpFail(self):
		"""mrpFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mrpFail'):
			from .MrpFail import MrpFailCls
			self._mrpFail = MrpFailCls(self._core, self._cmd_group)
		return self._mrpFail

	@property
	def mspFail(self):
		"""mspFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mspFail'):
			from .MspFail import MspFailCls
			self._mspFail = MspFailCls(self._core, self._cmd_group)
		return self._mspFail

	@property
	def ovld(self):
		"""ovld commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ovld'):
			from .Ovld import OvldCls
			self._ovld = OvldCls(self._core, self._cmd_group)
		return self._ovld

	@property
	def spDail(self):
		"""spDail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spDail'):
			from .SpDail import SpDailCls
			self._spDail = SpDailCls(self._core, self._cmd_group)
		return self._spDail

	@property
	def sstate(self):
		"""sstate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sstate'):
			from .Sstate import SstateCls
			self._sstate = SstateCls(self._core, self._cmd_group)
		return self._sstate

	@property
	def tsDelta(self):
		"""tsDelta commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsDelta'):
			from .TsDelta import TsDeltaCls
			self._tsDelta = TsDeltaCls(self._core, self._cmd_group)
		return self._tsDelta

	@property
	def tstamp(self):
		"""tstamp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tstamp'):
			from .Tstamp import TstampCls
			self._tstamp = TstampCls(self._core, self._cmd_group)
		return self._tstamp

	@property
	def tput(self):
		"""tput commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tput'):
			from .Tput import TputCls
			self._tput = TputCls(self._core, self._cmd_group)
		return self._tput

	def clone(self) -> 'SummaryCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SummaryCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
