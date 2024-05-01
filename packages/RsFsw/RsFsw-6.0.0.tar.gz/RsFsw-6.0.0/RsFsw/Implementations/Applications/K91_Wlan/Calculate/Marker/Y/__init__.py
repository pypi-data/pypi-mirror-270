from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class YCls:
	"""Y commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	@property
	def percent(self):
		"""percent commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_percent'):
			from .Percent import PercentCls
			self._percent = PercentCls(self._core, self._cmd_group)
		return self._percent

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:Y \n
		Snippet: value: float = driver.applications.k91Wlan.calculate.marker.y.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Queries the position of a marker on the y-axis. In result displays with a third aspect (for example 'EVM vs Symbol x
		Carrier') , you can also use the command to define the position of the marker on the y-axis. If necessary, the command
		activates the marker first. To get a valid result, you have to perform a complete measurement with synchronization to the
		end of the measurement before reading out the result. This is only possible for single measurement mode. See also method
		RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: yposition: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:Y?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'YCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = YCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
