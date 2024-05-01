from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhaseCls:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, type_py: enums.PhaseTrackingMethod) -> None:
		"""SCPI: [SENSe][:LTE]:DL:TRACking:PHASe \n
		Snippet: driver.applications.k10Xlte.sense.lte.downlink.tracking.phase.set(type_py = enums.PhaseTrackingMethod.OFF) \n
		Selects the phase tracking type. \n
			:param type_py: OFF Deactivate phase tracking PIL Pilot only PILP Pilot and payload
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.PhaseTrackingMethod)
		self._core.io.write(f'SENSe:LTE:DL:TRACking:PHASe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PhaseTrackingMethod:
		"""SCPI: [SENSe][:LTE]:DL:TRACking:PHASe \n
		Snippet: value: enums.PhaseTrackingMethod = driver.applications.k10Xlte.sense.lte.downlink.tracking.phase.get() \n
		Selects the phase tracking type. \n
			:return: type_py: OFF Deactivate phase tracking PIL Pilot only PILP Pilot and payload"""
		response = self._core.io.query_str(f'SENSe:LTE:DL:TRACking:PHASe?')
		return Conversions.str_to_scalar_enum(response, enums.PhaseTrackingMethod)
