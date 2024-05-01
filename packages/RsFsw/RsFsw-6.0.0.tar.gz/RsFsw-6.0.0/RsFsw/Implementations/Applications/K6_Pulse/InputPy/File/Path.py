from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PathCls:
	"""Path commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)

	def set(self, filename: str, analysis_bw: float = None) -> None:
		"""SCPI: INPut:FILE:PATH \n
		Snippet: driver.applications.k6Pulse.inputPy.file.path.set(filename = 'abc', analysis_bw = 1.0) \n
		Selects the I/Q data file to be used as input for further measurements.
			INTRO_CMD_HELP: The I/Q data file must be in one of the following supported formats: \n
			- .iq.tar
			- .iqw
			- .csv
			- .mat
			- .wv
			- .aid
		Only a single data stream or channel can be used as input, even if multiple streams or channels are stored in the file.
		For some file formats that do not provide the sample rate and measurement time or record length, you must define these
		parameters manually. Otherwise the traces are not visible in the result displays. For details, see 'Basics on Input from
		I/Q Data Files'. \n
			:param filename: String containing the path and name of the source file. The file type is determined by the file extension. If no file extension is provided, the file type is assumed to be .iq.tar. For .mat files, Matlab(R) v4 is assumed.
			:param analysis_bw: Optionally: The analysis bandwidth to be used by the measurement. The bandwidth must be smaller than or equal to the bandwidth of the data that was stored in the file. Unit: HZ
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filename', filename, DataType.String), ArgSingle('analysis_bw', analysis_bw, DataType.Float, None, is_optional=True))
		self._core.io.write(f'INPut:FILE:PATH {param}'.rstrip())

	# noinspection PyTypeChecker
	class PathStruct(StructBase):
		"""Response structure. Fields: \n
			- Filename: str: String containing the path and name of the source file. The file type is determined by the file extension. If no file extension is provided, the file type is assumed to be .iq.tar. For .mat files, Matlab(R) v4 is assumed.
			- Analysis_Bw: float: Optionally: The analysis bandwidth to be used by the measurement. The bandwidth must be smaller than or equal to the bandwidth of the data that was stored in the file. Unit: HZ"""
		__meta_args_list = [
			ArgStruct.scalar_str('Filename'),
			ArgStruct.scalar_float('Analysis_Bw')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Filename: str = None
			self.Analysis_Bw: float = None

	def get(self) -> PathStruct:
		"""SCPI: INPut:FILE:PATH \n
		Snippet: value: PathStruct = driver.applications.k6Pulse.inputPy.file.path.get() \n
		Selects the I/Q data file to be used as input for further measurements.
			INTRO_CMD_HELP: The I/Q data file must be in one of the following supported formats: \n
			- .iq.tar
			- .iqw
			- .csv
			- .mat
			- .wv
			- .aid
		Only a single data stream or channel can be used as input, even if multiple streams or channels are stored in the file.
		For some file formats that do not provide the sample rate and measurement time or record length, you must define these
		parameters manually. Otherwise the traces are not visible in the result displays. For details, see 'Basics on Input from
		I/Q Data Files'. \n
			:return: structure: for return value, see the help for PathStruct structure arguments."""
		return self._core.io.query_struct(f'INPut:FILE:PATH?', self.__class__.PathStruct())
