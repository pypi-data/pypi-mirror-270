from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandCls:
	"""Band commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("band", core, parent)

	def set(self, mode: enums.LowHigh, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:BAND \n
		Snippet: driver.applications.k149Uwb.sense.espectrum.msr.band.set(mode = enums.LowHigh.HIGH, subBlock = repcap.SubBlock.Default) \n
		Defines the frequency range of the bands used by the base station. \n
			:param mode: No help available
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.LowHigh)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:BAND {param}')

	# noinspection PyTypeChecker
	def get(self, subBlock=repcap.SubBlock.Default) -> enums.LowHigh:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:BAND \n
		Snippet: value: enums.LowHigh = driver.applications.k149Uwb.sense.espectrum.msr.band.get(subBlock = repcap.SubBlock.Default) \n
		Defines the frequency range of the bands used by the base station. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: mode: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)
