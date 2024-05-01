from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INPut:SELect:BBANalog[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.inputPy.select.bbAnalog.state.set(state = False) \n
		This command turns simultaneous use of RF input and analog baseband input on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:SELect:BBANalog:STATe {param}')

	def get(self) -> bool:
		"""SCPI: INPut:SELect:BBANalog[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.inputPy.select.bbAnalog.state.get() \n
		This command turns simultaneous use of RF input and analog baseband input on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'INPut:SELect:BBANalog:STATe?')
		return Conversions.str_to_bool(response)
