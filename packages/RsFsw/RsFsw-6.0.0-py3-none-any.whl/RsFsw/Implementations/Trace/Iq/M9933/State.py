from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: TRACe:IQ:M9933:STATe \n
		Snippet: driver.trace.iq.m9933.state.set(state = False) \n
		Enables the optional analysis bandwidth extensions B6001/B8001, if available, for a center frequency of 9.993 GHz. Note
		the restrictions described in 'Bandwidth extension options B6001 / B8001 at CF 9.933 GHz'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TRACe:IQ:M9933:STATe {param}')

	def get(self) -> bool:
		"""SCPI: TRACe:IQ:M9933:STATe \n
		Snippet: value: bool = driver.trace.iq.m9933.state.get() \n
		Enables the optional analysis bandwidth extensions B6001/B8001, if available, for a center frequency of 9.993 GHz. Note
		the restrictions described in 'Bandwidth extension options B6001 / B8001 at CF 9.933 GHz'. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'TRACe:IQ:M9933:STATe?')
		return Conversions.str_to_bool(response)
