from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RangeCls:
	"""Range commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	def set(self, range_py: enums.RangeK91) -> None:
		"""SCPI: [SENSe]:DEMod:CESTimation:RANGe \n
		Snippet: driver.applications.k91Wlan.sense.demod.cestimation.range.set(range_py = enums.RangeK91.PFTRacking) \n
		No command help available \n
			:param range_py: PRE1t | PRE2t | PFTRacking | PUTRacking PRE1t The channel estimation is performed using the preamble of the HE/EHT-LTF as required in the standard. PRE2t The channel estimation is performed using the preamble of both training fields. PFTRacking The channel estimation is performed using the preamble and the payload. The EVM results can be calculated more accurately. (Note: this setting corresponds to the [SENSe:]DEMod:CESTimation 1 command in previous firmware versions.) PUTRacking The channel estimation is performed using the preamble and the payload. The EVM results can be calculated more accurately. The user-defined tracking settings are applied to the payload symbols used for payload channel estimation (see 'Tracking and channel estimation') .
		"""
		param = Conversions.enum_scalar_to_str(range_py, enums.RangeK91)
		self._core.io.write(f'SENSe:DEMod:CESTimation:RANGe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.RangeK91:
		"""SCPI: [SENSe]:DEMod:CESTimation:RANGe \n
		Snippet: value: enums.RangeK91 = driver.applications.k91Wlan.sense.demod.cestimation.range.get() \n
		No command help available \n
			:return: range_py: PRE1t | PRE2t | PFTRacking | PUTRacking PRE1t The channel estimation is performed using the preamble of the HE/EHT-LTF as required in the standard. PRE2t The channel estimation is performed using the preamble of both training fields. PFTRacking The channel estimation is performed using the preamble and the payload. The EVM results can be calculated more accurately. (Note: this setting corresponds to the [SENSe:]DEMod:CESTimation 1 command in previous firmware versions.) PUTRacking The channel estimation is performed using the preamble and the payload. The EVM results can be calculated more accurately. The user-defined tracking settings are applied to the payload symbols used for payload channel estimation (see 'Tracking and channel estimation') ."""
		response = self._core.io.query_str(f'SENSe:DEMod:CESTimation:RANGe?')
		return Conversions.str_to_scalar_enum(response, enums.RangeK91)
