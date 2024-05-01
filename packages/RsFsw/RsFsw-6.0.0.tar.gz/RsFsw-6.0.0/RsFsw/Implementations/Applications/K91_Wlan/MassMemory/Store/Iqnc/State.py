from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, position: int, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:IQNC:STATe \n
		Snippet: driver.applications.k91Wlan.massMemory.store.iqnc.state.set(position = 1, filename = 'abc', store = repcap.Store.Default) \n
		Exports the I/Q data for a single PPDU with the analyzer noise removed to a file.
			INTRO_CMD_HELP: Prerequisites for this command: \n
			- Turn on I/Q noise cancellation. (See [SENSe:]ADJust:NCANcel:AVERage[:STATe]) . \n
			:param position: irrelevant
			:param filename: String containing the path and name of the file. The file extension is .iq.tar.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('position', position, DataType.Integer), ArgSingle('filename', filename, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:IQNC:STATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class StateStruct(StructBase):
		"""Response structure. Fields: \n
			- Position: int: No parameter help available
			- Filename: str: String containing the path and name of the file. The file extension is .iq.tar."""
		__meta_args_list = [
			ArgStruct.scalar_int('Position'),
			ArgStruct.scalar_str('Filename')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Position: int = None
			self.Filename: str = None

	def get(self, store=repcap.Store.Default) -> StateStruct:
		"""SCPI: MMEMory:STORe<n>:IQNC:STATe \n
		Snippet: value: StateStruct = driver.applications.k91Wlan.massMemory.store.iqnc.state.get(store = repcap.Store.Default) \n
		Exports the I/Q data for a single PPDU with the analyzer noise removed to a file.
			INTRO_CMD_HELP: Prerequisites for this command: \n
			- Turn on I/Q noise cancellation. (See [SENSe:]ADJust:NCANcel:AVERage[:STATe]) . \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: structure: for return value, see the help for StateStruct structure arguments."""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		return self._core.io.query_struct(f'MMEMory:STORe{store_cmd_val}:IQNC:STATe?', self.__class__.StateStruct())
