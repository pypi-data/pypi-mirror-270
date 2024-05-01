from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConnectorCls:
	"""Connector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connector", core, parent)

	def set(self, input_connectors: enums.InputConnectorC) -> None:
		"""SCPI: INPut:CONNector \n
		Snippet: driver.applications.k60Transient.inputPy.connector.set(input_connectors = enums.InputConnectorC.RF) \n
		Determines which connector the input for the measurement is taken from. For more information, see 'Receiving Data Input
		and Providing Data Output'. If an external frontend is active, the connector is automatically set to RF. \n
			:param input_connectors: RF RF input connector AIQI Analog Baseband I connector This setting is only available if the 'Analog Baseband' interface (FSW-B71) is installed and active for input. It is not available for the FSW67 or FSW85. RFPRobe Active RF probe
		"""
		param = Conversions.enum_scalar_to_str(input_connectors, enums.InputConnectorC)
		self._core.io.write(f'INPut:CONNector {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.InputConnectorC:
		"""SCPI: INPut:CONNector \n
		Snippet: value: enums.InputConnectorC = driver.applications.k60Transient.inputPy.connector.get() \n
		Determines which connector the input for the measurement is taken from. For more information, see 'Receiving Data Input
		and Providing Data Output'. If an external frontend is active, the connector is automatically set to RF. \n
			:return: input_connectors: No help available"""
		response = self._core.io.query_str(f'INPut:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.InputConnectorC)
