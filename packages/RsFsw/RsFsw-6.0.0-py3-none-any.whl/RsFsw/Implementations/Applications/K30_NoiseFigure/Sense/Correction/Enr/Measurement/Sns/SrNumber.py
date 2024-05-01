from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrNumberCls:
	"""SrNumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srNumber", core, parent)

	def set(self, serial_number: str) -> None:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:SNS:SRNumber \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.enr.measurement.sns.srNumber.set(serial_number = 'abc') \n
		Sets and queries the measurement noise source smart noise source serial number. \n
			:param serial_number: No help available
		"""
		param = Conversions.value_to_quoted_str(serial_number)
		self._core.io.write(f'SENSe:CORRection:ENR:MEASurement:SNS:SRNumber {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:SNS:SRNumber \n
		Snippet: value: str = driver.applications.k30NoiseFigure.sense.correction.enr.measurement.sns.srNumber.get() \n
		Sets and queries the measurement noise source smart noise source serial number. \n
			:return: serial_number: No help available"""
		response = self._core.io.query_str(f'SENSe:CORRection:ENR:MEASurement:SNS:SRNumber?')
		return trim_str_response(response)
