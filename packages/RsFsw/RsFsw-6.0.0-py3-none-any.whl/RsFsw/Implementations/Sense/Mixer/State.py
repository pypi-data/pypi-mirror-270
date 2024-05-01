from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:MIXer[:STATe] \n
		Snippet: driver.sense.mixer.state.set(state = False) \n
		Activates or deactivates the use of a connected external mixer as input for the measurement. This command is only
		available if the optional External Mixer is installed and an external mixer is connected. (See 'How to work with external
		mixers') . \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:MIXer:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:MIXer[:STATe] \n
		Snippet: value: bool = driver.sense.mixer.state.get() \n
		Activates or deactivates the use of a connected external mixer as input for the measurement. This command is only
		available if the optional External Mixer is installed and an external mixer is connected. (See 'How to work with external
		mixers') . \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:MIXer:STATe?')
		return Conversions.str_to_bool(response)
