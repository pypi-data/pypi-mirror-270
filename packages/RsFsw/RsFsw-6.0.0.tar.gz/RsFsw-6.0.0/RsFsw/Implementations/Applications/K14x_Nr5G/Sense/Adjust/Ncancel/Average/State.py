from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:ADJust:NCANcel:AVERage:STATe \n
		Snippet: driver.applications.k14Xnr5G.sense.adjust.ncancel.average.state.set(state = False) \n
		Enables and disables I/Q noise cancellation. Requires the R&S FSW-K575 option and a synchronized, repetitive input signal.
		The number of initial measurements performed is defined by [SENSe:]ADJust:NCANcel:AVERage[:COUNt]. For details, see
		'Concept of I/Q noise cancellation'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on If synchronization fails, the noise cancellation process is not started, and an error message is provided. Status bit 7 in the STATus:QUEStionable:SYNC:CONDition status register is set (BIT_K575_FAILED) . See method RsFsw.Status.Questionable.Sync.Condition.get_
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:ADJust:NCANcel:AVERage:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:ADJust:NCANcel:AVERage:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.adjust.ncancel.average.state.get() \n
		Enables and disables I/Q noise cancellation. Requires the R&S FSW-K575 option and a synchronized, repetitive input signal.
		The number of initial measurements performed is defined by [SENSe:]ADJust:NCANcel:AVERage[:COUNt]. For details, see
		'Concept of I/Q noise cancellation'. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on If synchronization fails, the noise cancellation process is not started, and an error message is provided. Status bit 7 in the STATus:QUEStionable:SYNC:CONDition status register is set (BIT_K575_FAILED) . See method RsFsw.Status.Questionable.Sync.Condition.get_"""
		response = self._core.io.query_str(f'SENSe:ADJust:NCANcel:AVERage:STATe?')
		return Conversions.str_to_bool(response)
