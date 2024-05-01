from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:MODeling[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.modeling.state.set(state = False) \n
		This command turns system modeling on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:MODeling:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:MODeling[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.modeling.state.get() \n
		This command turns system modeling on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:MODeling:STATe?')
		return Conversions.str_to_bool(response)
