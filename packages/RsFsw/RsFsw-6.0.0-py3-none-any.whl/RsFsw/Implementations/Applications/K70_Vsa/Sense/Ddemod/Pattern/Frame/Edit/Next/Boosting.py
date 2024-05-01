from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BoostingCls:
	"""Boosting commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("boosting", core, parent)

	def set(self, boosting: float) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:EDIT:NEXT:BOOSting \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.next.boosting.set(boosting = 1.0) \n
		Determines which boosting is used to demodulate the frame next to the last configured subframe. Is only available if the
		additional Multi-Modulation Analysis option (FSW-K70M) is installed. \n
			:param boosting: Range: 0.1 to 60
		"""
		param = Conversions.decimal_value_to_str(boosting)
		self._core.io.write(f'SENSe:DDEMod:PATTern:FRAMe:EDIT:NEXT:BOOSting {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:EDIT:NEXT:BOOSting \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.next.boosting.get() \n
		Determines which boosting is used to demodulate the frame next to the last configured subframe. Is only available if the
		additional Multi-Modulation Analysis option (FSW-K70M) is installed. \n
			:return: boosting: Range: 0.1 to 60"""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:FRAMe:EDIT:NEXT:BOOSting?')
		return Conversions.str_to_float(response)
