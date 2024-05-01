from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandCls:
	"""Band commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("band", core, parent)

	def set(self, band: enums.Band) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:BAND \n
		Snippet: driver.sense.correction.cvl.band.set(band = enums.Band.A) \n
		Defines the waveguide band for which the conversion loss table is to be used. This setting is checked against the current
		mixer setting before the table can be assigned to the range. Before this command can be performed, the conversion loss
		table must be selected (see [SENSe:]CORRection:CVL:SELect) . Is only available with option B21 (External Mixer) installed. \n
			:param band: K | KA | Q | U | V | E | W | F | D | G | Y | J | USER Standard waveguide band or user-defined band. For a definition of the frequency range for the pre-defined bands, see Table 'Frequency ranges for pre-defined bands') .
		"""
		param = Conversions.enum_scalar_to_str(band, enums.Band)
		self._core.io.write(f'SENSe:CORRection:CVL:BAND {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Band:
		"""SCPI: [SENSe]:CORRection:CVL:BAND \n
		Snippet: value: enums.Band = driver.sense.correction.cvl.band.get() \n
		Defines the waveguide band for which the conversion loss table is to be used. This setting is checked against the current
		mixer setting before the table can be assigned to the range. Before this command can be performed, the conversion loss
		table must be selected (see [SENSe:]CORRection:CVL:SELect) . Is only available with option B21 (External Mixer) installed. \n
			:return: band: K | KA | Q | U | V | E | W | F | D | G | Y | J | USER Standard waveguide band or user-defined band. For a definition of the frequency range for the pre-defined bands, see Table 'Frequency ranges for pre-defined bands') ."""
		response = self._core.io.query_str(f'SENSe:CORRection:CVL:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.Band)
