from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StaFrequencyCls:
	"""StaFrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("staFrequency", core, parent)

	def set(self, state: bool, scaling: enums.FrequencyScaling = None, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:STATe:STAFrequency \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.table.state.staFrequency.set(state = False, scaling = enums.FrequencyScaling.GHZ, window = repcap.Window.Default) \n
		If enabled, the hop state frequency parameter is included in the result tables (see 'State parameters') . Note that only
		the enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Table.Results.
		get_ query. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param scaling: GHZ | MHZ | KHZ | HZ Defines the scaling for the frequency parameters
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('scaling', scaling, DataType.Enum, enums.FrequencyScaling, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:STATe:STAFrequency {param}'.rstrip())

	# noinspection PyTypeChecker
	class StaFrequencyStruct(StructBase):
		"""Response structure. Fields: \n
			- State: bool: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			- Scaling: enums.FrequencyScaling: GHZ | MHZ | KHZ | HZ Defines the scaling for the frequency parameters"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State'),
			ArgStruct.scalar_enum('Scaling', enums.FrequencyScaling)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: bool = None
			self.Scaling: enums.FrequencyScaling = None

	def get(self, window=repcap.Window.Default) -> StaFrequencyStruct:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:STATe:STAFrequency \n
		Snippet: value: StaFrequencyStruct = driver.applications.k60Transient.calculate.hopDetection.table.state.staFrequency.get(window = repcap.Window.Default) \n
		If enabled, the hop state frequency parameter is included in the result tables (see 'State parameters') . Note that only
		the enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Table.Results.
		get_ query. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for StaFrequencyStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:STATe:STAFrequency?', self.__class__.StaFrequencyStruct())
