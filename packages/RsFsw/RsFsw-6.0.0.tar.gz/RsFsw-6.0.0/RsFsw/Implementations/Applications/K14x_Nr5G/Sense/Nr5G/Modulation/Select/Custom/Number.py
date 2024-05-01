from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NumberCls:
	"""Number commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("number", core, parent)

	def set(self, modulation: float) -> None:
		"""SCPI: [SENSe]:NR5G:MODulation:SELect:CUSTom:NUMBer \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.modulation.select.custom.number.set(modulation = 1.0) \n
		No command help available \n
			:param modulation: No help available
		"""
		param = Conversions.decimal_value_to_str(modulation)
		self._core.io.write(f'SENSe:NR5G:MODulation:SELect:CUSTom:NUMBer {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:NR5G:MODulation:SELect:CUSTom:NUMBer \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.nr5G.modulation.select.custom.number.get() \n
		No command help available \n
			:return: modulation: No help available"""
		response = self._core.io.query_str(f'SENSe:NR5G:MODulation:SELect:CUSTom:NUMBer?')
		return Conversions.str_to_float(response)
