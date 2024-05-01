from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ValueCls:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, gain: float) -> None:
		"""SCPI: INPut:GAIN[:VALue] \n
		Snippet: driver.applications.k40PhaseNoise.inputPy.gain.value.set(gain = 1.0) \n
		Selects the 'gain' if the preamplifier is activated (INP:GAIN:STAT ON, see method RsFsw.Applications.K10x_Lte.InputPy.
		Gain.State.set) . The command requires the additional preamplifier hardware option. \n
			:param gain: For all FSW models except for FSW85, the following settings are available: 15 dB and 30 dB All other values are rounded to the nearest of these two. For FSW85 models: FSW43 or higher: 30 dB Unit: DB
		"""
		param = Conversions.decimal_value_to_str(gain)
		self._core.io.write(f'INPut:GAIN:VALue {param}')

	def get(self) -> float:
		"""SCPI: INPut:GAIN[:VALue] \n
		Snippet: value: float = driver.applications.k40PhaseNoise.inputPy.gain.value.get() \n
		Selects the 'gain' if the preamplifier is activated (INP:GAIN:STAT ON, see method RsFsw.Applications.K10x_Lte.InputPy.
		Gain.State.set) . The command requires the additional preamplifier hardware option. \n
			:return: gain: For all FSW models except for FSW85, the following settings are available: 15 dB and 30 dB All other values are rounded to the nearest of these two. For FSW85 models: FSW43 or higher: 30 dB Unit: DB"""
		response = self._core.io.query_str(f'INPut:GAIN:VALue?')
		return Conversions.str_to_float(response)
