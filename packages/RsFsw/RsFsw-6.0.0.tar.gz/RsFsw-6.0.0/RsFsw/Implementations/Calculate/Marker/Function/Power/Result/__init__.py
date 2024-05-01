from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	@property
	def details(self):
		"""details commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_details'):
			from .Details import DetailsCls
			self._details = DetailsCls(self._core, self._cmd_group)
		return self._details

	@property
	def phz(self):
		"""phz commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phz'):
			from .Phz import PhzCls
			self._phz = PhzCls(self._core, self._cmd_group)
		return self._phz

	@property
	def unit(self):
		"""unit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import UnitCls
			self._unit = UnitCls(self._core, self._cmd_group)
		return self._unit

	def set(self, measurement: enums.MarkerFunctionA, window=repcap.Window.Default, marker=repcap.Marker.Default, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer<sb>:RESult \n
		Snippet: driver.calculate.marker.function.power.result.set(measurement = enums.MarkerFunctionA.ACPower, window = repcap.Window.Default, marker = repcap.Marker.Default, subBlock = repcap.SubBlock.Default) \n
		Queries the results of power measurements. To get a valid result, you have to perform a complete measurement with
		synchronization to the end of the measurement before reading out the result. This is only possible for single sweep mode.
		See also method RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param measurement: ACPower | MCACpower ACLR measurements (also known as adjacent channel power or multicarrier adjacent channel measurements) . Returns the power for every active transmission and adjacent channel. The order is: - power of the transmission channels - power of adjacent channel (lower,upper) - power of alternate channels (lower,upper) MSR ACLR results: For MSR ACLR measurements, the order of the returned results is slightly different: - power of the transmission channels - total power of the transmission channels for each sub block - power of adjacent channels (lower, upper) - power of alternate channels (lower, upper) - power of gap channels (lower1, upper1, lower2, upper2) The unit of the return values depends on the scaling of the y-axis: - logarithmic scaling returns the power in the current unit - linear scaling returns the power in W GACLr For MSR ACLR measurements only: returns a list of ACLR values for each gap channel (lower1, upper1, lower2, upper2) MACM For MSR ACLR measurements only: returns a list of CACLR values for each gap channel (lower1, upper1, lower2, upper2) See 'Gap channels and CACLR'. CN Carrier-to-noise measurements. Returns the C/N ratio in dB. CN0 Carrier-to-noise measurements. Returns the C/N ratio referenced to a 1 Hz bandwidth in dBm/Hz. CPOWer Channel power measurements. Returns the channel power. The unit of the return values depends on the scaling of the y-axis: - logarithmic scaling returns the power in the current unit - linear scaling returns the power in W For SEM measurements, the return value is the channel power of the reference range (in the specified sub block) . PPOWer Peak power measurements. Returns the peak power. The unit of the return values depends on the scaling of the y-axis: - logarithmic scaling returns the power in the current unit - linear scaling returns the power in W For SEM measurements, the return value is the peak power of the reference range (in the specified sub block) . Note that this result is only available if the power reference type is set to peak power (see [SENSe:]ESPectrumsb:RTYPe) . OBANdwidth | OBWidth Occupied bandwidth. Returns the occupied bandwidth in Hz. COBandwidth | COBWidth Centroid frequency,Frequency offset See 'OBW results'
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Power')
		"""
		param = Conversions.enum_scalar_to_str(measurement, enums.MarkerFunctionA)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer{subBlock_cmd_val}:RESult {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default, subBlock=repcap.SubBlock.Default) -> enums.MarkerFunctionA:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer<sb>:RESult \n
		Snippet: value: enums.MarkerFunctionA = driver.calculate.marker.function.power.result.get(window = repcap.Window.Default, marker = repcap.Marker.Default, subBlock = repcap.SubBlock.Default) \n
		Queries the results of power measurements. To get a valid result, you have to perform a complete measurement with
		synchronization to the end of the measurement before reading out the result. This is only possible for single sweep mode.
		See also method RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Power')
			:return: measurement: ACPower | MCACpower ACLR measurements (also known as adjacent channel power or multicarrier adjacent channel measurements) . Returns the power for every active transmission and adjacent channel. The order is: - power of the transmission channels - power of adjacent channel (lower,upper) - power of alternate channels (lower,upper) MSR ACLR results: For MSR ACLR measurements, the order of the returned results is slightly different: - power of the transmission channels - total power of the transmission channels for each sub block - power of adjacent channels (lower, upper) - power of alternate channels (lower, upper) - power of gap channels (lower1, upper1, lower2, upper2) The unit of the return values depends on the scaling of the y-axis: - logarithmic scaling returns the power in the current unit - linear scaling returns the power in W GACLr For MSR ACLR measurements only: returns a list of ACLR values for each gap channel (lower1, upper1, lower2, upper2) MACM For MSR ACLR measurements only: returns a list of CACLR values for each gap channel (lower1, upper1, lower2, upper2) See 'Gap channels and CACLR'. CN Carrier-to-noise measurements. Returns the C/N ratio in dB. CN0 Carrier-to-noise measurements. Returns the C/N ratio referenced to a 1 Hz bandwidth in dBm/Hz. CPOWer Channel power measurements. Returns the channel power. The unit of the return values depends on the scaling of the y-axis: - logarithmic scaling returns the power in the current unit - linear scaling returns the power in W For SEM measurements, the return value is the channel power of the reference range (in the specified sub block) . PPOWer Peak power measurements. Returns the peak power. The unit of the return values depends on the scaling of the y-axis: - logarithmic scaling returns the power in the current unit - linear scaling returns the power in W For SEM measurements, the return value is the peak power of the reference range (in the specified sub block) . Note that this result is only available if the power reference type is set to peak power (see [SENSe:]ESPectrumsb:RTYPe) . OBANdwidth | OBWidth Occupied bandwidth. Returns the occupied bandwidth in Hz. COBandwidth | COBWidth Centroid frequency,Frequency offset See 'OBW results'"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer{subBlock_cmd_val}:RESult?')
		return Conversions.str_to_scalar_enum(response, enums.MarkerFunctionA)

	def clone(self) -> 'ResultCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResultCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
