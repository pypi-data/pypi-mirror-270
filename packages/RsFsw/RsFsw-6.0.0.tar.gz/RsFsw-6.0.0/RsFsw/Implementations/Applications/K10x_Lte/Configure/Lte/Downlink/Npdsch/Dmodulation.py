from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DmodulationCls:
	"""Dmodulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmodulation", core, parent)

	def set(self, demodulation: bool) -> None:
		"""SCPI: CONFigure[:LTE]:DL:NPDSch:DMODulation \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.npdsch.dmodulation.set(demodulation = False) \n
		No command help available \n
			:param demodulation: No help available
		"""
		param = Conversions.bool_to_str(demodulation)
		self._core.io.write(f'CONFigure:LTE:DL:NPDSch:DMODulation {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure[:LTE]:DL:NPDSch:DMODulation \n
		Snippet: value: bool = driver.applications.k10Xlte.configure.lte.downlink.npdsch.dmodulation.get() \n
		No command help available \n
			:return: demodulation: No help available"""
		response = self._core.io.query_str(f'CONFigure:LTE:DL:NPDSch:DMODulation?')
		return Conversions.str_to_bool(response)
