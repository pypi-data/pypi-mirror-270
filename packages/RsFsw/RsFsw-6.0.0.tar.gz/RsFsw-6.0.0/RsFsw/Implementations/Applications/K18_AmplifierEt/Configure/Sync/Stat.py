from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StatCls:
	"""Stat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stat", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:SYNC:STAT \n
		Snippet: driver.applications.k18AmplifierEt.configure.sync.stat.set(state = False) \n
		This command turns synchronization between reference and measured signal on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:SYNC:STAT {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:SYNC:STAT \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.sync.stat.get() \n
		This command turns synchronization between reference and measured signal on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:SYNC:STAT?')
		return Conversions.str_to_bool(response)
