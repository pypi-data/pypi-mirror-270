from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ImmediateCls:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:BURSt:SPECtrum:FLATness[:IMMediate] \n
		Snippet: driver.applications.k91Wlan.configure.burst.spectrum.flatness.immediate.set() \n
		This remote control command configures the result display in window 2 to be 'Spectrum Flatness' or 'Group Delay',
		depending on which result display was selected last using method RsFsw.Applications.K91_Wlan.Configure.Burst.Spectrum.
		Flatness.Select.set. Results are only displayed after a measurement is executed, e.g. using the method RsFsw.Applications.
		K10x_Lte.Initiate.Immediate.set command. Note that the CONF:BURS:<ResultType>:IMM commands change the screen layout to
		display the 'Magnitude Capture' buffer in window 1 at the top of the screen and the selected result type in window 2
		below that. Any other active windows are closed. Use the LAYout commands to change the display (see 'Working with windows
		in the display') . \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:BURSt:SPECtrum:FLATness:IMMediate', opc_timeout_ms)
