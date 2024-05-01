from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RestoreCls:
	"""Restore commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("restore", core, parent)

	def set(self, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:PRESet:RESTore \n
		Snippet: driver.sense.espectrum.preset.restore.set(subBlock = repcap.SubBlock.Default) \n
		Restores the default configurations of predefined SEM standards. Note that the command will overwrite customized
		standards that have the same name as predefined standards. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:PRESet:RESTore')

	def set_with_opc(self, subBlock=repcap.SubBlock.Default, opc_timeout_ms: int = -1) -> None:
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		"""SCPI: [SENSe]:ESPectrum<sb>:PRESet:RESTore \n
		Snippet: driver.sense.espectrum.preset.restore.set_with_opc(subBlock = repcap.SubBlock.Default) \n
		Restores the default configurations of predefined SEM standards. Note that the command will overwrite customized
		standards that have the same name as predefined standards. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:ESPectrum{subBlock_cmd_val}:PRESet:RESTore', opc_timeout_ms)
