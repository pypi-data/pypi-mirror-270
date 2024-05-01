from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ValueCls:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, harm_order: float) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic:HIGH[:VALue] \n
		Snippet: driver.applications.k14Xnr5G.sense.mixer.harmonic.high.value.set(harm_order = 1.0) \n
		Specifies the harmonic order to be used for the high (second) range. \n
			:param harm_order: Range: 2 to 128 (USER band) ; for other bands: see band definition
		"""
		param = Conversions.decimal_value_to_str(harm_order)
		self._core.io.write(f'SENSe:MIXer:HARMonic:HIGH:VALue {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:HARMonic:HIGH[:VALue] \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.mixer.harmonic.high.value.get() \n
		Specifies the harmonic order to be used for the high (second) range. \n
			:return: harm_order: Range: 2 to 128 (USER band) ; for other bands: see band definition"""
		response = self._core.io.query_str(f'SENSe:MIXer:HARMonic:HIGH:VALue?')
		return Conversions.str_to_float(response)
