from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NtransitionCls:
	"""Ntransition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ntransition", core, parent)

	def set(self, bit_definition: int, channel_name: str = None) -> None:
		"""SCPI: STATus:QUEStionable:CALibration:NTRansition \n
		Snippet: driver.status.questionable.calibration.ntransition.set(bit_definition = 1, channel_name = 'abc') \n
		No command help available \n
			:param bit_definition: No help available
			:param channel_name: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('bit_definition', bit_definition, DataType.Integer), ArgSingle('channel_name', channel_name, DataType.String, None, is_optional=True))
		self._core.io.write(f'STATus:QUEStionable:CALibration:NTRansition {param}'.rstrip())

	# noinspection PyTypeChecker
	class NtransitionStruct(StructBase):
		"""Response structure. Fields: \n
			- Bit_Definition: int: No parameter help available
			- Channel_Name: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Bit_Definition'),
			ArgStruct.scalar_str('Channel_Name')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bit_Definition: int = None
			self.Channel_Name: str = None

	def get(self) -> NtransitionStruct:
		"""SCPI: STATus:QUEStionable:CALibration:NTRansition \n
		Snippet: value: NtransitionStruct = driver.status.questionable.calibration.ntransition.get() \n
		No command help available \n
			:return: structure: for return value, see the help for NtransitionStruct structure arguments."""
		return self._core.io.query_struct(f'STATus:QUEStionable:CALibration:NTRansition?', self.__class__.NtransitionStruct())
