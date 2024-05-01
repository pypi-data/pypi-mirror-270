from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MorderCls:
	"""Morder commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("morder", core, parent)

	def set(self, arg_0: float) -> None:
		"""SCPI: CONFigure:DPD:AMPM:MORDer \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.amPm.morder.set(arg_0 = 1.0) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'CONFigure:DPD:AMPM:MORDer {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:DPD:AMPM:MORDer \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.dpd.amPm.morder.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'CONFigure:DPD:AMPM:MORDer?')
		return Conversions.str_to_float(response)
