from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: MMEMory:LOAD:IQ:STATe \n
		Snippet: driver.massMemory.load.iq.state.set(filename = 'abc') \n
		Restores I/Q data from a file. \n
			:param filename: string String containing the path and name of the source file. The file type is determined by the file extension. If no file extension is provided, the file type is assumed to be .iq.tar. For .mat files, Matlab(R) v4 is assumed.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write_with_opc(f'MMEMory:LOAD:IQ:STATe 1, {param}')
