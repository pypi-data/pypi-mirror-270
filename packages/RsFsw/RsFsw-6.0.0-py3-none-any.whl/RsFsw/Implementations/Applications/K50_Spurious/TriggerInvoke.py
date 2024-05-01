from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TriggerInvokeCls:
	"""TriggerInvoke commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("triggerInvoke", core, parent)

	def set(self) -> None:
		"""SCPI: *TRG \n
		Snippet: driver.applications.k50Spurious.triggerInvoke.set() \n
		Trigger Triggers all actions waiting for a trigger event. In particular, *TRG generates a manual trigger signal.
		This common command complements the commands of the TRIGger subsystem. *TRG corresponds to the INITiate:IMMediate command.
		(See method RsFsw.Applications.K10x_Lte.Initiate.Immediate.set.) \n
		"""
		self._core.io.write(f'*TRG')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: *TRG \n
		Snippet: driver.applications.k50Spurious.triggerInvoke.set_with_opc() \n
		Trigger Triggers all actions waiting for a trigger event. In particular, *TRG generates a manual trigger signal.
		This common command complements the commands of the TRIGger subsystem. *TRG corresponds to the INITiate:IMMediate command.
		(See method RsFsw.Applications.K10x_Lte.Initiate.Immediate.set.) \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'*TRG', opc_timeout_ms)
