from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, opt_mode: enums.AttenuatorMode) -> None:
		"""SCPI: INPut:ATTenuation:AUTO:MODE \n
		Snippet: driver.inputPy.attenuation.auto.mode.set(opt_mode = enums.AttenuatorMode.LDIStortion) \n
		Selects the priority for signal processing after the RF attenuation has been applied. \n
			:param opt_mode: LNOise | LDIStortion LNOise Optimized for high sensitivity and low noise levels LDIStortion Optimized for low distortion by avoiding intermodulation
		"""
		param = Conversions.enum_scalar_to_str(opt_mode, enums.AttenuatorMode)
		self._core.io.write(f'INPut:ATTenuation:AUTO:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AttenuatorMode:
		"""SCPI: INPut:ATTenuation:AUTO:MODE \n
		Snippet: value: enums.AttenuatorMode = driver.inputPy.attenuation.auto.mode.get() \n
		Selects the priority for signal processing after the RF attenuation has been applied. \n
			:return: opt_mode: LNOise | LDIStortion LNOise Optimized for high sensitivity and low noise levels LDIStortion Optimized for low distortion by avoiding intermodulation"""
		response = self._core.io.query_str(f'INPut:ATTenuation:AUTO:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AttenuatorMode)
