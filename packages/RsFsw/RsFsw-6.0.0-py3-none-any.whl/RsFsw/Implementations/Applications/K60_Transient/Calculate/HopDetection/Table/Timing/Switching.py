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
class SwitchingCls:
	"""Switching commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("switching", core, parent)

	def set(self, state: bool, scaling: enums.TimeScaling = None, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:TIMing:SWITching \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.table.timing.switching.set(state = False, scaling = enums.TimeScaling.MS, window = repcap.Window.Default) \n
		If enabled, the specified time parameter is included in the result tables (see 'Timing parameters') . Note that only the
		enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Table.Results.
		get_ query. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The parameter is included. ON | 1 The parameter is not included
			:param scaling: S | MS | US | NS Defines the scaling for the timing parameters
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('scaling', scaling, DataType.Enum, enums.TimeScaling, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:TIMing:SWITching {param}'.rstrip())

	# noinspection PyTypeChecker
	class SwitchingStruct(StructBase):
		"""Response structure. Fields: \n
			- State: bool: ON | OFF | 0 | 1 OFF | 0 The parameter is included. ON | 1 The parameter is not included
			- Scaling: enums.TimeScaling: S | MS | US | NS Defines the scaling for the timing parameters"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State'),
			ArgStruct.scalar_enum('Scaling', enums.TimeScaling)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: bool = None
			self.Scaling: enums.TimeScaling = None

	def get(self, window=repcap.Window.Default) -> SwitchingStruct:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:TIMing:SWITching \n
		Snippet: value: SwitchingStruct = driver.applications.k60Transient.calculate.hopDetection.table.timing.switching.get(window = repcap.Window.Default) \n
		If enabled, the specified time parameter is included in the result tables (see 'Timing parameters') . Note that only the
		enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Table.Results.
		get_ query. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for SwitchingStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:TIMing:SWITching?', self.__class__.SwitchingStruct())
