from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, frequency: List[float], level: List[float], window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MASK:LOWer[:DATA] \n
		Snippet: driver.calculate.mask.lower.data.set(frequency = [1.1, 2.2, 3.3], level = [1.1, 2.2, 3.3], window = repcap.Window.Default) \n
		Defines the shape of the lower frequency mask. Before making any changes to a frequency mask, you have to select one by
		name with method RsFsw.Calculate.Mask.Name.set. The unit of the power levels depends on method RsFsw.Calculate.Mask.Mode.
		set. For R&S FSW-K70, this command is query only. [N] pairs of numerical values. [N] is the number of data points the
		mask consists of. Each data point is defined by the frequency and the level. All values are separated by commas.
		Note that the data points have to be inside the current span. \n
			:param frequency: Frequency of the data point Unit: Hz
			:param level: Level of the data point Unit: DBM
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('frequency', frequency, DataType.FloatList, None), ArgSingle.as_open_list('level', level, DataType.FloatList, None))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MASK:LOWer:DATA {param}'.rstrip())

	# noinspection PyTypeChecker
	class DataStruct(StructBase):
		"""Response structure. Fields: \n
			- Frequency: List[float]: Frequency of the data point Unit: Hz
			- Level: List[float]: Level of the data point Unit: DBM"""
		__meta_args_list = [
			ArgStruct('Frequency', DataType.FloatList, None, False, True, 1),
			ArgStruct('Level', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency: List[float] = None
			self.Level: List[float] = None

	def get(self, window=repcap.Window.Default) -> DataStruct:
		"""SCPI: CALCulate<n>:MASK:LOWer[:DATA] \n
		Snippet: value: DataStruct = driver.calculate.mask.lower.data.get(window = repcap.Window.Default) \n
		Defines the shape of the lower frequency mask. Before making any changes to a frequency mask, you have to select one by
		name with method RsFsw.Calculate.Mask.Name.set. The unit of the power levels depends on method RsFsw.Calculate.Mask.Mode.
		set. For R&S FSW-K70, this command is query only. [N] pairs of numerical values. [N] is the number of data points the
		mask consists of. Each data point is defined by the frequency and the level. All values are separated by commas.
		Note that the data points have to be inside the current span. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for DataStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:MASK:LOWer:DATA?', self.__class__.DataStruct())
