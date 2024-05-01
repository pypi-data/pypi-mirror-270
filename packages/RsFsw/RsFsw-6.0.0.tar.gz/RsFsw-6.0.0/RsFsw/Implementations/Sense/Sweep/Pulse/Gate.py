from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GateCls:
	"""Gate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gate", core, parent)

	def set(self, gate_source: enums.GateSource) -> None:
		"""SCPI: [SENSe]:SWEep:PULSe:GATE \n
		Snippet: driver.sense.sweep.pulse.gate.set(gate_source = enums.GateSource.EXTernal) \n
		No command help available \n
			:param gate_source: No help available
		"""
		param = Conversions.enum_scalar_to_str(gate_source, enums.GateSource)
		self._core.io.write(f'SENSe:SWEep:PULSe:GATE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.GateSource:
		"""SCPI: [SENSe]:SWEep:PULSe:GATE \n
		Snippet: value: enums.GateSource = driver.sense.sweep.pulse.gate.get() \n
		No command help available \n
			:return: gate_source: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:PULSe:GATE?')
		return Conversions.str_to_scalar_enum(response, enums.GateSource)
