from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowerCls:
	"""Lower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lower", core, parent)

	def set(self, threshold: float) -> None:
		"""SCPI: [SENSe]:ADJust:CONFigure:HYSTeresis:LOWer \n
		Snippet: driver.sense.adjust.configure.hysteresis.lower.set(threshold = 1.0) \n
		When the reference level is adjusted automatically using the [SENSe:]ADJust:LEVel command, the internal attenuators and
		the preamplifier are also adjusted. To avoid frequent adaptation due to small changes in the input signal, you can define
		a hysteresis. This setting defines a lower threshold the signal must fall below (compared to the last measurement) before
		the reference level is adapted automatically. This setting can only be adjusted in the MSRA primary application, not in
		the secondary applications. \n
			:param threshold: Range: 0 dB to 200 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'SENSe:ADJust:CONFigure:HYSTeresis:LOWer {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADJust:CONFigure:HYSTeresis:LOWer \n
		Snippet: value: float = driver.sense.adjust.configure.hysteresis.lower.get() \n
		When the reference level is adjusted automatically using the [SENSe:]ADJust:LEVel command, the internal attenuators and
		the preamplifier are also adjusted. To avoid frequent adaptation due to small changes in the input signal, you can define
		a hysteresis. This setting defines a lower threshold the signal must fall below (compared to the last measurement) before
		the reference level is adapted automatically. This setting can only be adjusted in the MSRA primary application, not in
		the secondary applications. \n
			:return: threshold: Range: 0 dB to 200 dB, Unit: dB"""
		response = self._core.io.query_str(f'SENSe:ADJust:CONFigure:HYSTeresis:LOWer?')
		return Conversions.str_to_float(response)
