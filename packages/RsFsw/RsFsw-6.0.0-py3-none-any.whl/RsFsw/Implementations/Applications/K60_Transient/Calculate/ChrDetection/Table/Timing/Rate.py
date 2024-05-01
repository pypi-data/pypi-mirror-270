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
class RateCls:
	"""Rate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	def set(self, state: bool, scaling: enums.FreqTimeScaling = None, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:CHRDetection:TABLe:TIMing:RATE \n
		Snippet: driver.applications.k60Transient.calculate.chrDetection.table.timing.rate.set(state = False, scaling = enums.FreqTimeScaling.GHZ_us, window = repcap.Window.Default) \n
		No command help available \n
			:param state: 1..n
			:param scaling: S | MS | US | NS
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('scaling', scaling, DataType.Enum, enums.FreqTimeScaling, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:CHRDetection:TABLe:TIMing:RATE {param}'.rstrip())

	# noinspection PyTypeChecker
	class RateStruct(StructBase):
		"""Response structure. Fields: \n
			- State: bool: No parameter help available
			- Scaling: enums.FreqTimeScaling: S | MS | US | NS"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State'),
			ArgStruct.scalar_enum('Scaling', enums.FreqTimeScaling)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: bool = None
			self.Scaling: enums.FreqTimeScaling = None

	def get(self, window=repcap.Window.Default) -> RateStruct:
		"""SCPI: CALCulate<n>:CHRDetection:TABLe:TIMing:RATE \n
		Snippet: value: RateStruct = driver.applications.k60Transient.calculate.chrDetection.table.timing.rate.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for RateStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:CHRDetection:TABLe:TIMing:RATE?', self.__class__.RateStruct())
