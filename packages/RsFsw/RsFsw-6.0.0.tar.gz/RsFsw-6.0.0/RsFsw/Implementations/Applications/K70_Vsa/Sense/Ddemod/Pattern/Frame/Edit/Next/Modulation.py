from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	def set(self, modulation: enums.FrameModulation) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:EDIT:NEXT:MODulation \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.next.modulation.set(modulation = enums.FrameModulation.AUTO) \n
		Determines which modulation type is used to demodulate the frame after to the last configured subframe. Is only available
		if the additional Multi-Modulation Analysis option (FSW-K70M) is installed. \n
			:param modulation: AUTO | DATA | PATTern Data The modulation type defined for data symbols is used (see [SENSe:]DDEMod:MAPPing[:VALue]) Pattern The modulation type defined for pattern symbols is used (see [SENSe:]DDEMod:PATTern:MAPPing[:VALue]) . Auto The nextt frame uses the same modulation as the first subframe of the frame configuration.
		"""
		param = Conversions.enum_scalar_to_str(modulation, enums.FrameModulation)
		self._core.io.write(f'SENSe:DDEMod:PATTern:FRAMe:EDIT:NEXT:MODulation {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FrameModulation:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:EDIT:NEXT:MODulation \n
		Snippet: value: enums.FrameModulation = driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.next.modulation.get() \n
		Determines which modulation type is used to demodulate the frame after to the last configured subframe. Is only available
		if the additional Multi-Modulation Analysis option (FSW-K70M) is installed. \n
			:return: modulation: AUTO | DATA | PATTern Data The modulation type defined for data symbols is used (see [SENSe:]DDEMod:MAPPing[:VALue]) Pattern The modulation type defined for pattern symbols is used (see [SENSe:]DDEMod:PATTern:MAPPing[:VALue]) . Auto The nextt frame uses the same modulation as the first subframe of the frame configuration."""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:FRAMe:EDIT:NEXT:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.FrameModulation)
