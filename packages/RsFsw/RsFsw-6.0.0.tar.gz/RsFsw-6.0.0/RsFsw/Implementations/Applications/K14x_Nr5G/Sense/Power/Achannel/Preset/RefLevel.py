from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefLevelCls:
	"""RefLevel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refLevel", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:PRESet:RLEVel \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.preset.refLevel.set() \n
		This command determines the ideal reference level for the current measurement. This automatic routine makes sure that the
		that the signal power level does not overload the FSW or limit the dynamic range by too small a S/N ratio. To determine
		the best reference level, the FSW aborts current measurements and performs a series of test sweeps. After it has finished
		the test, it continues with the actual measurement. To get a valid result, you have to perform a complete sweep with
		synchronization to the sweep end. This is only possible in single sweep mode. \n
		"""
		self._core.io.write(f'SENSe:POWer:ACHannel:PRESet:RLEVel')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:PRESet:RLEVel \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.preset.refLevel.set_with_opc() \n
		This command determines the ideal reference level for the current measurement. This automatic routine makes sure that the
		that the signal power level does not overload the FSW or limit the dynamic range by too small a S/N ratio. To determine
		the best reference level, the FSW aborts current measurements and performs a series of test sweeps. After it has finished
		the test, it continues with the actual measurement. To get a valid result, you have to perform a complete sweep with
		synchronization to the sweep end. This is only possible in single sweep mode. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:POWer:ACHannel:PRESet:RLEVel', opc_timeout_ms)
