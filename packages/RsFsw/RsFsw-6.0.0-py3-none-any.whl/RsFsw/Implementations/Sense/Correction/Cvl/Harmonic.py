from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HarmonicCls:
	"""Harmonic commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("harmonic", core, parent)

	def set(self, harm_order: float) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:HARMonic \n
		Snippet: driver.sense.correction.cvl.harmonic.set(harm_order = 1.0) \n
		Defines the harmonic order for which the conversion loss table is to be used. This setting is checked against the current
		mixer setting before the table can be assigned to the range. Before this command can be performed, the conversion loss
		table must be selected (see [SENSe:]CORRection:CVL:SELect. Is only available with option B21 (External Mixer) installed. \n
			:param harm_order: Range: 2 to 65
		"""
		param = Conversions.decimal_value_to_str(harm_order)
		self._core.io.write(f'SENSe:CORRection:CVL:HARMonic {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:CVL:HARMonic \n
		Snippet: value: float = driver.sense.correction.cvl.harmonic.get() \n
		Defines the harmonic order for which the conversion loss table is to be used. This setting is checked against the current
		mixer setting before the table can be assigned to the range. Before this command can be performed, the conversion loss
		table must be selected (see [SENSe:]CORRection:CVL:SELect. Is only available with option B21 (External Mixer) installed. \n
			:return: harm_order: Range: 2 to 65"""
		response = self._core.io.query_str(f'SENSe:CORRection:CVL:HARMonic?')
		return Conversions.str_to_float(response)
