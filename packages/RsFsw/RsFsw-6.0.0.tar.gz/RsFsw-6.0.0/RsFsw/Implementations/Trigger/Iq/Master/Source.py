from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SourceCls:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, dev_name: str, ms_trig_iq_master_source: enums.TriggerPort) -> None:
		"""SCPI: TRIGger:IQ:MASTer:SOURce \n
		Snippet: driver.trigger.iq.master.source.set(dev_name = 'abc', ms_trig_iq_master_source = enums.TriggerPort.EXT1) \n
		No command help available \n
			:param dev_name: No help available
			:param ms_trig_iq_master_source: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('dev_name', dev_name, DataType.String), ArgSingle('ms_trig_iq_master_source', ms_trig_iq_master_source, DataType.Enum, enums.TriggerPort))
		self._core.io.write(f'TRIGger:IQ:MASTer:SOURce {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self) -> enums.TriggerPort:
		"""SCPI: TRIGger:IQ:MASTer:SOURce \n
		Snippet: value: enums.TriggerPort = driver.trigger.iq.master.source.get() \n
		No command help available \n
			:return: ms_trig_iq_master_source: No help available"""
		response = self._core.io.query_str(f'TRIGger:IQ:MASTer:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerPort)
