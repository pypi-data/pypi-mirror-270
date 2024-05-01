from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefreshCls:
	"""Refresh commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refresh", core, parent)

	def set(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:REFResh \n
		Snippet: driver.initiate.refresh.set() \n
		Updates the current measurement results to reflect the current measurement settings. No new I/Q data is captured. Thus,
		measurement settings apply to the I/Q data currently in the capture buffer. The command applies exclusively to I/Q
		measurements. It requires I/Q data. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:REFResh', opc_timeout_ms)
