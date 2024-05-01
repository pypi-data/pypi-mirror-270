from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EspectrumCls:
	"""Espectrum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("espectrum", core, parent)

	def set(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:ESPectrum \n
		Snippet: driver.initiate.espectrum.set() \n
		Initiates a Spectrum Emission Mask measurement. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:ESPectrum', opc_timeout_ms)
