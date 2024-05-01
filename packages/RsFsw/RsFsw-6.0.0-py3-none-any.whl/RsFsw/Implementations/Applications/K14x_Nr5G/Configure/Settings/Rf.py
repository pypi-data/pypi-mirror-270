from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfCls:
	"""Rf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rf", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:SETTings:RF \n
		Snippet: driver.applications.k14Xnr5G.configure.settings.rf.set() \n
		Downloads the RF settings (frequency, level) from the generator to the analyzer.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) . \n
		"""
		self._core.io.write(f'CONFigure:SETTings:RF')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:SETTings:RF \n
		Snippet: driver.applications.k14Xnr5G.configure.settings.rf.set_with_opc() \n
		Downloads the RF settings (frequency, level) from the generator to the analyzer.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:SETTings:RF', opc_timeout_ms)
