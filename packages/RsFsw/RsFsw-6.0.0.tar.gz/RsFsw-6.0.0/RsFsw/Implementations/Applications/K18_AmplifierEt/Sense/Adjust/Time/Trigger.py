from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TriggerCls:
	"""Trigger commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:ADJust:TIME:TRIGger \n
		Snippet: driver.applications.k18AmplifierEt.sense.adjust.time.trigger.set() \n
		Calculates the time trigger. \n
		"""
		self._core.io.write(f'SENSe:ADJust:TIME:TRIGger')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:ADJust:TIME:TRIGger \n
		Snippet: driver.applications.k18AmplifierEt.sense.adjust.time.trigger.set_with_opc() \n
		Calculates the time trigger. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:ADJust:TIME:TRIGger', opc_timeout_ms)
