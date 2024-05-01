from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PresetCls:
	"""Preset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preset", core, parent)

	def set(self, standard: str, window=repcap.Window.Default, marker=repcap.Marker.Default, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer<sb>:PRESet \n
		Snippet: driver.applications.k10Xlte.calculate.marker.function.power.preset.set(standard = 'abc', window = repcap.Window.Default, marker = repcap.Marker.Default, subBlock = repcap.SubBlock.Default) \n
		Loads a measurement configuration. The measurement configuration for power measurements consists of weighting filter,
		channel bandwidth and spacing, resolution and video bandwidth, detector and sweep time. If the 'Multi-Standard Radio'
		standard is selected (see 'Standard') , different commands are required to configure ACLR measurements (see 'Configuring
		MSR ACLR measurements') . \n
			:param standard: For more information see 'Reference: predefined CP/ACLR standards'. If you want to load a customized configuration, the parameter is a string containing the file name.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Power')
		"""
		param = Conversions.value_to_quoted_str(standard)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer{subBlock_cmd_val}:PRESet {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default, subBlock=repcap.SubBlock.Default) -> str:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer<sb>:PRESet \n
		Snippet: value: str = driver.applications.k10Xlte.calculate.marker.function.power.preset.get(window = repcap.Window.Default, marker = repcap.Marker.Default, subBlock = repcap.SubBlock.Default) \n
		Loads a measurement configuration. The measurement configuration for power measurements consists of weighting filter,
		channel bandwidth and spacing, resolution and video bandwidth, detector and sweep time. If the 'Multi-Standard Radio'
		standard is selected (see 'Standard') , different commands are required to configure ACLR measurements (see 'Configuring
		MSR ACLR measurements') . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Power')
			:return: standard: For more information see 'Reference: predefined CP/ACLR standards'. If you want to load a customized configuration, the parameter is a string containing the file name."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer{subBlock_cmd_val}:PRESet?')
		return trim_str_response(response)
