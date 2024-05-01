from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StatisticsCls:
	"""Statistics commands group definition. 7 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("statistics", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	@property
	def cumulativeDistribFnc(self):
		"""cumulativeDistribFnc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cumulativeDistribFnc'):
			from .CumulativeDistribFnc import CumulativeDistribFncCls
			self._cumulativeDistribFnc = CumulativeDistribFncCls(self._core, self._cmd_group)
		return self._cumulativeDistribFnc

	@property
	def scale(self):
		"""scale commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_scale'):
			from .Scale import ScaleCls
			self._scale = ScaleCls(self._core, self._cmd_group)
		return self._scale

	def preset(self, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:STATistics:PRESet \n
		Snippet: driver.applications.k70Vsa.calculate.statistics.preset(window = repcap.Window.Default) \n
		Resets the scale of the diagram (x- and y-axis) .
			INTRO_CMD_HELP: The I/Q data file must be in one of the following supported formats: \n
			- Reference level (x-axis) 0.0 dBm
			- Display range (x-axis) for APD measurements 100 dB
			- Display range (x-axis) for CCDF measurements 20 dB
			- Upper limit of the y-axis 1.0
			- Lower limit of the y-axis 1E-6 \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:STATistics:PRESet')

	def preset_with_opc(self, window=repcap.Window.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		"""SCPI: CALCulate<n>:STATistics:PRESet \n
		Snippet: driver.applications.k70Vsa.calculate.statistics.preset_with_opc(window = repcap.Window.Default) \n
		Resets the scale of the diagram (x- and y-axis) .
			INTRO_CMD_HELP: The I/Q data file must be in one of the following supported formats: \n
			- Reference level (x-axis) 0.0 dBm
			- Display range (x-axis) for APD measurements 100 dB
			- Display range (x-axis) for CCDF measurements 20 dB
			- Upper limit of the y-axis 1.0
			- Lower limit of the y-axis 1E-6 \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:STATistics:PRESet', opc_timeout_ms)

	def clone(self) -> 'StatisticsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StatisticsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
