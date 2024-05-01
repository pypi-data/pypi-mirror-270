from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 13 total commands, 7 Subgroups, 1 group commands
	Repeated Capability: SubBlock, default value after init: SubBlock.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_subBlock_get', 'repcap_subBlock_set', repcap.SubBlock.Nr1)

	def repcap_subBlock_set(self, subBlock: repcap.SubBlock) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SubBlock.Default
		Default value after init: SubBlock.Nr1"""
		self._cmd_group.set_repcap_enum_value(subBlock)

	def repcap_subBlock_get(self) -> repcap.SubBlock:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import SelectCls
			self._select = SelectCls(self._core, self._cmd_group)
		return self._select

	@property
	def result(self):
		"""result commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def restore(self):
		"""restore commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_restore'):
			from .Restore import RestoreCls
			self._restore = RestoreCls(self._core, self._cmd_group)
		return self._restore

	@property
	def standard(self):
		"""standard commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_standard'):
			from .Standard import StandardCls
			self._standard = StandardCls(self._core, self._cmd_group)
		return self._standard

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	@property
	def auto(self):
		"""auto commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	def preset(self, standard: enums.TechnologyStandardB, window=repcap.Window.Default, marker=repcap.Marker.Default, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer<sb>:PRESet \n
		Snippet: driver.calculate.marker.function.power.preset(standard = enums.TechnologyStandardB.AWLan, window = repcap.Window.Default, marker = repcap.Marker.Default, subBlock = repcap.SubBlock.Default) \n
		Loads a measurement configuration. The measurement configuration for power measurements consists of weighting filter,
		channel bandwidth and spacing, resolution and video bandwidth, detector and sweep time. If the 'Multi-Standard Radio'
		standard is selected (see 'Standard') , different commands are required to configure ACLR measurements (see 'Configuring
		MSR ACLR measurements') . \n
			:param standard: (enum or string) For more information see 'Reference: predefined CP/ACLR standards'. If you want to load a customized configuration, the parameter is a string containing the file name.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Power')
		"""
		param = Conversions.enum_ext_scalar_to_str(standard, enums.TechnologyStandardB)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer{subBlock_cmd_val}:PRESet {param}')

	def clone(self) -> 'PowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
