from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, arg_0: bool) -> None:
		"""SCPI: INSTrument:COUPle:GENerator:CENTer[:STATe] \n
		Snippet: driver.instrument.couple.generator.center.state.set(arg_0 = False) \n
		Couples the center frequency of the connected signal generator to the FSW. This command requires the method RsFsw.
		Instrument.Couple.Generator.State.set to be ON. \n
			:param arg_0: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'INSTrument:COUPle:GENerator:CENTer:STATe {param}')

	def get(self) -> bool:
		"""SCPI: INSTrument:COUPle:GENerator:CENTer[:STATe] \n
		Snippet: value: bool = driver.instrument.couple.generator.center.state.get() \n
		Couples the center frequency of the connected signal generator to the FSW. This command requires the method RsFsw.
		Instrument.Couple.Generator.State.set to be ON. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'INSTrument:COUPle:GENerator:CENTer:STATe?')
		return Conversions.str_to_bool(response)
