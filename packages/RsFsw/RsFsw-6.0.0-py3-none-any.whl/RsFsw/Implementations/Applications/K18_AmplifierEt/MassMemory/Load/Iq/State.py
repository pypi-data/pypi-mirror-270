from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, position: int, filename: str) -> None:
		"""SCPI: MMEMory:LOAD:IQ:STATe \n
		Snippet: driver.applications.k18AmplifierEt.massMemory.load.iq.state.set(position = 1, filename = 'abc') \n
		Restores I/Q data from a file. \n
			:param position: No help available
			:param filename: string String containing the path and name of the source file. The file type is determined by the file extension. If no file extension is provided, the file type is assumed to be .iq.tar. For .mat files, Matlab(R) v4 is assumed.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('position', position, DataType.Integer), ArgSingle('filename', filename, DataType.String))
		self._core.io.write(f'MMEMory:LOAD:IQ:STATe {param}'.rstrip())
