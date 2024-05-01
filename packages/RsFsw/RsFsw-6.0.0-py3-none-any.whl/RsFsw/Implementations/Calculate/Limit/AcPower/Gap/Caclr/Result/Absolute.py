from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AbsoluteCls:
	"""Absolute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Lower_Gap_Ab: float: No parameter help available
			- Upper_Gap_Ab: float: No parameter help available
			- Lower_Gap_Bc: float: No parameter help available
			- Upper_Gap_Bc: float: No parameter help available
			- Lower_Gap_Cd: float: No parameter help available
			- Upper_Gap_Cd: float: No parameter help available
			- Lower_Gap_De: float: No parameter help available
			- Upper_Gap_De: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Lower_Gap_Ab'),
			ArgStruct.scalar_float('Upper_Gap_Ab'),
			ArgStruct.scalar_float('Lower_Gap_Bc'),
			ArgStruct.scalar_float('Upper_Gap_Bc'),
			ArgStruct.scalar_float('Lower_Gap_Cd'),
			ArgStruct.scalar_float('Upper_Gap_Cd'),
			ArgStruct.scalar_float('Lower_Gap_De'),
			ArgStruct.scalar_float('Upper_Gap_De')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower_Gap_Ab: float = None
			self.Upper_Gap_Ab: float = None
			self.Lower_Gap_Bc: float = None
			self.Upper_Gap_Bc: float = None
			self.Lower_Gap_Cd: float = None
			self.Upper_Gap_Cd: float = None
			self.Lower_Gap_De: float = None
			self.Upper_Gap_De: float = None

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, gapChannel=repcap.GapChannel.Default) -> GetStruct:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:GAP<gap>[:CACLr]:RESult:ABSolute \n
		Snippet: value: GetStruct = driver.calculate.limit.acPower.gap.caclr.result.absolute.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, gapChannel = repcap.GapChannel.Default) \n
		Queries the absolute limit check results for the gap channels (MC ACLR measurements) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select absolute limit check mode evaluation mode ACLR: method RsFsw.Calculate.Limit.AcPower.Pmode.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:GAP{gapChannel_cmd_val}:CACLr:RESult:ABSolute?', self.__class__.GetStruct())
