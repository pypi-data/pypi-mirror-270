from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CreateCls:
	"""Create commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("create", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:GENerator:NPRatio:AWGN:CREate \n
		Snippet: driver.configure.generator.npratio.awgn.create.set() \n
		No command help available \n
		"""
		self._core.io.write(f'CONFigure:GENerator:NPRatio:AWGN:CREate')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:GENerator:NPRatio:AWGN:CREate \n
		Snippet: driver.configure.generator.npratio.awgn.create.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:GENerator:NPRatio:AWGN:CREate', opc_timeout_ms)
