from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RelativeCls:
	"""Relative commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def set(self, lower_limit: float, upper_limit: float = None, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:ACHannel[:RELative] \n
		Snippet: driver.applications.k14Xnr5G.calculate.limit.acPower.achannel.relative.set(lower_limit = 1.0, upper_limit = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Defines the relative limit of the adjacent channels. The reference value for the relative limit is the measured channel
		power. If you have defined an absolute limit as well as a relative limit, the FSW uses the lower value for the limit
		check. \n
			:param lower_limit: The limit of the lower adjacent channel. Range: 0 dB to 100 dB, Unit: dB
			:param upper_limit: The limit of the upper adjacent channel. Range: 0 dB to 100 dB, Unit: dB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('lower_limit', lower_limit, DataType.Float), ArgSingle('upper_limit', upper_limit, DataType.Float, None, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:ACHannel:RELative {param}'.rstrip())

	# noinspection PyTypeChecker
	class RelativeStruct(StructBase):
		"""Response structure. Fields: \n
			- Lower_Limit: float: The limit of the lower adjacent channel. Range: 0 dB to 100 dB, Unit: dB
			- Upper_Limit: float: The limit of the upper adjacent channel. Range: 0 dB to 100 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Lower_Limit'),
			ArgStruct.scalar_float('Upper_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower_Limit: float = None
			self.Upper_Limit: float = None

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> RelativeStruct:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:ACHannel[:RELative] \n
		Snippet: value: RelativeStruct = driver.applications.k14Xnr5G.calculate.limit.acPower.achannel.relative.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Defines the relative limit of the adjacent channels. The reference value for the relative limit is the measured channel
		power. If you have defined an absolute limit as well as a relative limit, the FSW uses the lower value for the limit
		check. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: structure: for return value, see the help for RelativeStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:ACHannel:RELative?', self.__class__.RelativeStruct())

	def clone(self) -> 'RelativeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RelativeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
