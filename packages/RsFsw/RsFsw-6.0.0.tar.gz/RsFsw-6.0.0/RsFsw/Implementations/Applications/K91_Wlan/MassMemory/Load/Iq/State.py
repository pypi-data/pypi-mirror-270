from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: int, filename: str) -> None:
		"""SCPI: MMEMory:LOAD:IQ:STATe \n
		Snippet: driver.applications.k91Wlan.massMemory.load.iq.state.set(state = 1, filename = 'abc') \n
		Restores I/Q data from a file. \n
			:param state: No help available
			:param filename: string String containing the path and name of the source file. The file type is determined by the file extension. If no file extension is provided, the file type is assumed to be .iq.tar. For .mat files, Matlab(R) v4 is assumed.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Integer), ArgSingle('filename', filename, DataType.String))
		self._core.io.write(f'MMEMory:LOAD:IQ:STATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class StateStruct(StructBase):
		"""Response structure. Fields: \n
			- State: int: No parameter help available
			- Filename: str: string String containing the path and name of the source file. The file type is determined by the file extension. If no file extension is provided, the file type is assumed to be .iq.tar. For .mat files, Matlab(R) v4 is assumed."""
		__meta_args_list = [
			ArgStruct.scalar_int('State'),
			ArgStruct.scalar_str('Filename')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: int = None
			self.Filename: str = None

	def get(self) -> StateStruct:
		"""SCPI: MMEMory:LOAD:IQ:STATe \n
		Snippet: value: StateStruct = driver.applications.k91Wlan.massMemory.load.iq.state.get() \n
		Restores I/Q data from a file. \n
			:return: structure: for return value, see the help for StateStruct structure arguments."""
		return self._core.io.query_struct(f'MMEMory:LOAD:IQ:STATe?', self.__class__.StateStruct())
