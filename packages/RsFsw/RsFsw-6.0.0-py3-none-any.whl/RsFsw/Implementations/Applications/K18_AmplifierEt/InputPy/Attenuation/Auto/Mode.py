from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, signal_path_mode: enums.SignalPathMode) -> None:
		"""SCPI: INPut:ATTenuation:AUTO:MODE \n
		Snippet: driver.applications.k18AmplifierEt.inputPy.attenuation.auto.mode.set(signal_path_mode = enums.SignalPathMode.LDIS) \n
		Selects the priority for signal processing after the RF attenuation has been applied. \n
			:param signal_path_mode: LNOise | LDIStortion LNOise Optimized for high sensitivity and low noise levels LDIStortion Optimized for low distortion by avoiding intermodulation
		"""
		param = Conversions.enum_scalar_to_str(signal_path_mode, enums.SignalPathMode)
		self._core.io.write(f'INPut:ATTenuation:AUTO:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SignalPathMode:
		"""SCPI: INPut:ATTenuation:AUTO:MODE \n
		Snippet: value: enums.SignalPathMode = driver.applications.k18AmplifierEt.inputPy.attenuation.auto.mode.get() \n
		Selects the priority for signal processing after the RF attenuation has been applied. \n
			:return: signal_path_mode: No help available"""
		response = self._core.io.query_str(f'INPut:ATTenuation:AUTO:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SignalPathMode)
