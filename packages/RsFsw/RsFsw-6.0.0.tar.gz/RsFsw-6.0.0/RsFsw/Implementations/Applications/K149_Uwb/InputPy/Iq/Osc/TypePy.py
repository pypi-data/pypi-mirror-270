from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.IqType) -> None:
		"""SCPI: INPut:IQ:OSC:TYPE \n
		Snippet: driver.applications.k149Uwb.inputPy.iq.osc.typePy.set(type_py = enums.IqType.Ipart=I) \n
		Defines the format of the input signal. \n
			:param type_py: IQ | I IQ Both components of the complex input signal (in-phase component, quadrature component) are filtered and resampled to the sample rate of the application. The input signal is down-converted with the center frequency (Low IF I) . I The input signal at the channel providing I data is resampled to the sample rate of the application. The input signal is down-converted with the center frequency (Low IF I) .
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.IqType)
		self._core.io.write(f'INPut:IQ:OSC:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.IqType:
		"""SCPI: INPut:IQ:OSC:TYPE \n
		Snippet: value: enums.IqType = driver.applications.k149Uwb.inputPy.iq.osc.typePy.get() \n
		Defines the format of the input signal. \n
			:return: type_py: IQ | I IQ Both components of the complex input signal (in-phase component, quadrature component) are filtered and resampled to the sample rate of the application. The input signal is down-converted with the center frequency (Low IF I) . I The input signal at the channel providing I data is resampled to the sample rate of the application. The input signal is down-converted with the center frequency (Low IF I) ."""
		response = self._core.io.query_str(f'INPut:IQ:OSC:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.IqType)
