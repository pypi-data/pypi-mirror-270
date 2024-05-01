from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, data_type: enums.IqType) -> None:
		"""SCPI: INPut:IQ:TYPE \n
		Snippet: driver.applications.k10Xlte.inputPy.iq.typePy.set(data_type = enums.IqType.Ipart=I) \n
		Defines the format of the input signal. \n
			:param data_type: IQ | I | Q IQ The input signal is filtered and resampled to the sample rate of the application. Two input channels are required for each input signal, one for the in-phase component, and one for the quadrature component. I The in-phase component of the input signal is filtered and resampled to the sample rate of the application. If the center frequency is not 0, the in-phase component of the input signal is down-converted first (Low IF I) . Q The quadrature component of the input signal is filtered and resampled to the sample rate of the application. If the center frequency is not 0, the quadrature component of the input signal is down-converted first (Low IF Q) .
		"""
		param = Conversions.enum_scalar_to_str(data_type, enums.IqType)
		self._core.io.write(f'INPut:IQ:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.IqType:
		"""SCPI: INPut:IQ:TYPE \n
		Snippet: value: enums.IqType = driver.applications.k10Xlte.inputPy.iq.typePy.get() \n
		Defines the format of the input signal. \n
			:return: data_type: IQ | I | Q IQ The input signal is filtered and resampled to the sample rate of the application. Two input channels are required for each input signal, one for the in-phase component, and one for the quadrature component. I The in-phase component of the input signal is filtered and resampled to the sample rate of the application. If the center frequency is not 0, the in-phase component of the input signal is down-converted first (Low IF I) . Q The quadrature component of the input signal is filtered and resampled to the sample rate of the application. If the center frequency is not 0, the quadrature component of the input signal is down-converted first (Low IF Q) ."""
		response = self._core.io.query_str(f'INPut:IQ:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.IqType)
