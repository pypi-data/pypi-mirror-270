from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PresetCls:
	"""Preset commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preset", core, parent)

	@property
	def refLevel(self):
		"""refLevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_refLevel'):
			from .RefLevel import RefLevelCls
			self._refLevel = RefLevelCls(self._core, self._cmd_group)
		return self._refLevel

	def set(self, measurement: enums.MeasurementK91) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:PRESet \n
		Snippet: driver.applications.k91Wlan.sense.power.achannel.preset.set(measurement = enums.MeasurementK91.ACPower) \n
		Determines the ideal span, bandwidths and detector for the current power measurement. To get a valid result, you have to
		perform a complete measurement with synchronization to the end of the measurement before reading out the result. This is
		only possible for single sweep mode. See also method RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param measurement: ACPower | MCACpower ACLR measurement CPOWer channel power measurement OBANdwidth | OBWidth Occupied bandwidth measurement CN Carrier to noise ratio CN0 Carrier to noise ration referenced to a 1 Hz bandwidth
		"""
		param = Conversions.enum_scalar_to_str(measurement, enums.MeasurementK91)
		self._core.io.write(f'SENSe:POWer:ACHannel:PRESet {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.MeasurementK91:
		"""SCPI: [SENSe]:POWer:ACHannel:PRESet \n
		Snippet: value: enums.MeasurementK91 = driver.applications.k91Wlan.sense.power.achannel.preset.get() \n
		Determines the ideal span, bandwidths and detector for the current power measurement. To get a valid result, you have to
		perform a complete measurement with synchronization to the end of the measurement before reading out the result. This is
		only possible for single sweep mode. See also method RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. \n
			:return: measurement: ACPower | MCACpower ACLR measurement CPOWer channel power measurement OBANdwidth | OBWidth Occupied bandwidth measurement CN Carrier to noise ratio CN0 Carrier to noise ration referenced to a 1 Hz bandwidth"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:PRESet?')
		return Conversions.str_to_scalar_enum(response, enums.MeasurementK91)

	def clone(self) -> 'PresetCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PresetCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
