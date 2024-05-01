from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MarkerCls:
	"""Marker commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: MarkerDestination, default value after init: MarkerDestination.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("marker", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_markerDestination_get', 'repcap_markerDestination_set', repcap.MarkerDestination.Nr1)

	def repcap_markerDestination_set(self, markerDestination: repcap.MarkerDestination) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to MarkerDestination.Default
		Default value after init: MarkerDestination.Nr1"""
		self._cmd_group.set_repcap_enum_value(markerDestination)

	def repcap_markerDestination_get(self) -> repcap.MarkerDestination:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, state: bool, window=repcap.Window.Default, marker=repcap.Marker.Default, markerDestination=repcap.MarkerDestination.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m1>:LINK:TO:MARKer<m2> \n
		Snippet: driver.applications.k50Spurious.calculate.marker.linkTo.marker.set(state = False, window = repcap.Window.Default, marker = repcap.Marker.Default, markerDestination = repcap.MarkerDestination.Default) \n
		Links the normal source marker <ms> to any active destination marker <md> (normal or delta marker) . If you change the
		horizontal position of marker <md>, marker <ms> changes its horizontal position to the same value. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param markerDestination: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		markerDestination_cmd_val = self._cmd_group.get_repcap_cmd_value(markerDestination, repcap.MarkerDestination)
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:LINK:TO:MARKer{markerDestination_cmd_val} {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default, markerDestination=repcap.MarkerDestination.Default) -> bool:
		"""SCPI: CALCulate<n>:MARKer<m1>:LINK:TO:MARKer<m2> \n
		Snippet: value: bool = driver.applications.k50Spurious.calculate.marker.linkTo.marker.get(window = repcap.Window.Default, marker = repcap.Marker.Default, markerDestination = repcap.MarkerDestination.Default) \n
		Links the normal source marker <ms> to any active destination marker <md> (normal or delta marker) . If you change the
		horizontal position of marker <md>, marker <ms> changes its horizontal position to the same value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param markerDestination: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		markerDestination_cmd_val = self._cmd_group.get_repcap_cmd_value(markerDestination, repcap.MarkerDestination)
		response = self._core.io.query_str_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:LINK:TO:MARKer{markerDestination_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'MarkerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MarkerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
