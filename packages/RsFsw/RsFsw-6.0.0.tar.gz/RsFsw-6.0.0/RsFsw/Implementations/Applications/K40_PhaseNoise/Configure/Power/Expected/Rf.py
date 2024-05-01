from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfCls:
	"""Rf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rf", core, parent)

	def set(self, arg_0: float) -> None:
		"""SCPI: CONFigure:POWer:EXPected:RF \n
		Snippet: driver.applications.k40PhaseNoise.configure.power.expected.rf.set(arg_0 = 1.0) \n
		Specifies the mean power level of the source signal as supplied to the instrument's RF input. This value is overwritten
		if 'Auto Level' mode is turned on. \n
			:param arg_0: Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'CONFigure:POWer:EXPected:RF {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:POWer:EXPected:RF \n
		Snippet: value: float = driver.applications.k40PhaseNoise.configure.power.expected.rf.get() \n
		Specifies the mean power level of the source signal as supplied to the instrument's RF input. This value is overwritten
		if 'Auto Level' mode is turned on. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'CONFigure:POWer:EXPected:RF?')
		return Conversions.str_to_float(response)
