from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CoefficientsCls:
	"""Coefficients commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coefficients", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: MMEMory:LOAD:MDPD:APPLy:COEFficients \n
		Snippet: driver.applications.k18AmplifierEt.massMemory.load.mdpd.apply.coefficients.set(filename = 'abc') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'MMEMory:LOAD:MDPD:APPLy:COEFficients {param}')
