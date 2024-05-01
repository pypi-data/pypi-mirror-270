from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PresetCls:
	"""Preset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preset", core, parent)

	def set(self, standard: enums.StandardNr5GExt, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer:PRESet \n
		Snippet: driver.applications.k14Xnr5G.calculate.marker.function.power.preset.set(standard = enums.StandardNr5GExt.AWLan, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Loads a measurement configuration. The measurement configuration for power measurements consists of weighting filter,
		channel bandwidth and spacing, resolution and video bandwidth, detector and sweep time. If the 'Multi-Standard Radio'
		standard is selected (see 'Standard') , different commands are required to configure ACLR measurements (see 'Configuring
		MSR ACLR measurements') . \n
			:param standard: (enum or string) For more information see 'Reference: predefined CP/ACLR standards'. If you want to load a customized configuration, the parameter is a string containing the file name.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.enum_ext_scalar_to_str(standard, enums.StandardNr5GExt)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer:PRESet {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> enums.StandardNr5GExt:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer:PRESet \n
		Snippet: value: enums.StandardNr5GExt = driver.applications.k14Xnr5G.calculate.marker.function.power.preset.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Loads a measurement configuration. The measurement configuration for power measurements consists of weighting filter,
		channel bandwidth and spacing, resolution and video bandwidth, detector and sweep time. If the 'Multi-Standard Radio'
		standard is selected (see 'Standard') , different commands are required to configure ACLR measurements (see 'Configuring
		MSR ACLR measurements') . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: standard: (enum or string) For more information see 'Reference: predefined CP/ACLR standards'. If you want to load a customized configuration, the parameter is a string containing the file name."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer:PRESet?')
		return Conversions.str_to_scalar_enum_ext(response, enums.StandardNr5GExt)
