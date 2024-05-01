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

	def set(self, number: int, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:IQ:STATe \n
		Snippet: driver.applications.k9X11Ad.massMemory.store.iq.state.set(number = 1, filename = 'abc', store = repcap.Store.Default) \n
		Writes the captured I/Q data to a file. By default, the contents of the file are in 32-bit floating point format. \n
			:param number: 1..n
			:param filename: String containing the path and name of the target file. The file type is determined by the file extension. If no file extension is provided, the file type is assumed to be .iq.tar. For .mat files, Matlab(R) v4 is assumed.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('number', number, DataType.Integer), ArgSingle('filename', filename, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:IQ:STATe {param}'.rstrip())
