from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, position: float, filename: str, window=repcap.Window.Default) -> None:
		"""SCPI: MMEMory:LOAD<n>:IQ:STATe \n
		Snippet: driver.applications.k70Vsa.massMemory.load.iq.state.set(position = 1.0, filename = 'abc', window = repcap.Window.Default) \n
		Restores I/Q data from a file. \n
			:param position: No help available
			:param filename: string String containing the path and name of the source file. The file type is determined by the file extension. If no file extension is provided, the file type is assumed to be .iq.tar. For .mat files, Matlab(R) v4 is assumed.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Load')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('position', position, DataType.Float), ArgSingle('filename', filename, DataType.String))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'MMEMory:LOAD{window_cmd_val}:IQ:STATe {param}'.rstrip())
