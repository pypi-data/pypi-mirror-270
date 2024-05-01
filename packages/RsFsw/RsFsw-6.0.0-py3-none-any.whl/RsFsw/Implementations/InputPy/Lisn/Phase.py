from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhaseCls:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, phase: enums.LisnPhase) -> None:
		"""SCPI: INPut:LISN:PHASe \n
		Snippet: driver.inputPy.lisn.phase.set(phase = enums.LisnPhase.L1) \n
		Selects one LISN phase to be measured. \n
			:param phase: L1 L2 Available for networks with four phases (R&S ESH2Z5, R&S ENV4200 and R&S ENV432) L3 Available for networks with four phases (R&S ESH2Z5, R&S ENV4200 and R&S ENV432) N
		"""
		param = Conversions.enum_scalar_to_str(phase, enums.LisnPhase)
		self._core.io.write(f'INPut:LISN:PHASe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.LisnPhase:
		"""SCPI: INPut:LISN:PHASe \n
		Snippet: value: enums.LisnPhase = driver.inputPy.lisn.phase.get() \n
		Selects one LISN phase to be measured. \n
			:return: phase: L1 L2 Available for networks with four phases (R&S ESH2Z5, R&S ENV4200 and R&S ENV432) L3 Available for networks with four phases (R&S ESH2Z5, R&S ENV4200 and R&S ENV432) N"""
		response = self._core.io.query_str(f'INPut:LISN:PHASe?')
		return Conversions.str_to_scalar_enum(response, enums.LisnPhase)
