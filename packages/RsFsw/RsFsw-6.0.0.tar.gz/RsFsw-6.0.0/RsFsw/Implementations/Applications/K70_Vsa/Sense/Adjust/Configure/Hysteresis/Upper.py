from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UpperCls:
	"""Upper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upper", core, parent)

	def set(self, hysteresis_upper: float) -> None:
		"""SCPI: [SENSe]:ADJust:CONFigure[:HYSTeresis]:UPPer \n
		Snippet: driver.applications.k70Vsa.sense.adjust.configure.hysteresis.upper.set(hysteresis_upper = 1.0) \n
		When the reference level is adjusted automatically using the [SENSe:]ADJust:LEVel command, the internal attenuators and
		the preamplifier are also adjusted. To avoid frequent adaptation due to small changes in the input signal, you can define
		a hysteresis. This setting defines an upper threshold the signal must exceed (compared to the last measurement) before
		the reference level is adapted automatically. This setting can only be adjusted in the MSRA primary application, not in
		the secondary applications. \n
			:param hysteresis_upper: Range: 0 dB to 200 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(hysteresis_upper)
		self._core.io.write(f'SENSe:ADJust:CONFigure:HYSTeresis:UPPer {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADJust:CONFigure[:HYSTeresis]:UPPer \n
		Snippet: value: float = driver.applications.k70Vsa.sense.adjust.configure.hysteresis.upper.get() \n
		When the reference level is adjusted automatically using the [SENSe:]ADJust:LEVel command, the internal attenuators and
		the preamplifier are also adjusted. To avoid frequent adaptation due to small changes in the input signal, you can define
		a hysteresis. This setting defines an upper threshold the signal must exceed (compared to the last measurement) before
		the reference level is adapted automatically. This setting can only be adjusted in the MSRA primary application, not in
		the secondary applications. \n
			:return: hysteresis_upper: No help available"""
		response = self._core.io.query_str(f'SENSe:ADJust:CONFigure:HYSTeresis:UPPer?')
		return Conversions.str_to_float(response)
