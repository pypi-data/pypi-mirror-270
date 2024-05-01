from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UnitCls:
	"""Unit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	def set(self, result: enums.EtResultUnit) -> None:
		"""SCPI: CONFigure:POWer:UNIT \n
		Snippet: driver.applications.k18AmplifierEt.configure.power.unit.set(result = enums.EtResultUnit.DBM) \n
		Switches the unit for power results from dBm (default) to Watts. \n
			:param result: DBM | WATT
		"""
		param = Conversions.enum_scalar_to_str(result, enums.EtResultUnit)
		self._core.io.write(f'CONFigure:POWer:UNIT {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.EtResultUnit:
		"""SCPI: CONFigure:POWer:UNIT \n
		Snippet: value: enums.EtResultUnit = driver.applications.k18AmplifierEt.configure.power.unit.get() \n
		Switches the unit for power results from dBm (default) to Watts. \n
			:return: result: DBM | WATT"""
		response = self._core.io.query_str(f'CONFigure:POWer:UNIT?')
		return Conversions.str_to_scalar_enum(response, enums.EtResultUnit)
