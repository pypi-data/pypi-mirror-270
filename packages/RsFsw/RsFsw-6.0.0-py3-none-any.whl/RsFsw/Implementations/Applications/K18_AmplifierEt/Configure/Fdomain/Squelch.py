from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SquelchCls:
	"""Squelch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("squelch", core, parent)

	def set(self, squelch_level: float) -> None:
		"""SCPI: CONFigure:FDOMain:SQUelch \n
		Snippet: driver.applications.k18AmplifierEt.configure.fdomain.squelch.set(squelch_level = 1.0) \n
		For group delay results, defines a level threshold below which the group delay is set to 0. If the group delay does not
		exceed the threshold, it is ignored altogether. \n
			:param squelch_level: Range: -200 to +200, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(squelch_level)
		self._core.io.write(f'CONFigure:FDOMain:SQUelch {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:FDOMain:SQUelch \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.fdomain.squelch.get() \n
		For group delay results, defines a level threshold below which the group delay is set to 0. If the group delay does not
		exceed the threshold, it is ignored altogether. \n
			:return: squelch_level: Range: -200 to +200, Unit: dBm"""
		response = self._core.io.query_str(f'CONFigure:FDOMain:SQUelch?')
		return Conversions.str_to_float(response)
