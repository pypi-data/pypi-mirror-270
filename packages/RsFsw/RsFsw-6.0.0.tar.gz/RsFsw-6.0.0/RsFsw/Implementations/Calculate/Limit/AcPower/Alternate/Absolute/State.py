from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state_lower: bool, state_upper: bool = None, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:ALTernate<ch>:ABSolute:STATe \n
		Snippet: driver.calculate.limit.acPower.alternate.absolute.state.set(state_lower = False, state_upper = False, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, channel = repcap.Channel.Default) \n
		This command turns the absolute limit check for the alternate channels on and off. You have to activate the general ACLR
		limit check before using this command with method RsFsw.Calculate.Limit.AcPower.State.set. \n
			:param state_lower: No help available
			:param state_upper: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Alternate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state_lower', state_lower, DataType.Boolean), ArgSingle('state_upper', state_upper, DataType.Boolean, None, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:ALTernate{channel_cmd_val}:ABSolute:STATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class State(StructBase):
		"""Response structure. Fields: \n
			- State_Lower: bool: No parameter help available
			- State_Upper: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State_Lower'),
			ArgStruct.scalar_bool('State_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State_Lower: bool = None
			self.State_Upper: bool = None

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, channel=repcap.Channel.Default) -> State:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:ALTernate<ch>:ABSolute:STATe \n
		Snippet: value: State = driver.calculate.limit.acPower.alternate.absolute.state.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, channel = repcap.Channel.Default) \n
		This command turns the absolute limit check for the alternate channels on and off. You have to activate the general ACLR
		limit check before using this command with method RsFsw.Calculate.Limit.AcPower.State.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Alternate')
			:return: structure: for return value, see the help for State structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:ALTernate{channel_cmd_val}:ABSolute:STATe?', self.__class__.State())
