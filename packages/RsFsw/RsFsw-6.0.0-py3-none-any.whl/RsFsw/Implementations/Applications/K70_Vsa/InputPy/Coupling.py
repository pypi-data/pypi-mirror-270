from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CouplingCls:
	"""Coupling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupling", core, parent)

	def set(self, input_coupling: enums.CouplingTypeA) -> None:
		"""SCPI: INPut:COUPling \n
		Snippet: driver.applications.k70Vsa.inputPy.coupling.set(input_coupling = enums.CouplingTypeA.AC) \n
		Selects the coupling type of the RF input. The command is not available for measurements with the optional 'Digital
		Baseband' interface. If an external frontend is active, the coupling is automatically set to AC. \n
			:param input_coupling: AC | DC AC AC coupling DC DC coupling
		"""
		param = Conversions.enum_scalar_to_str(input_coupling, enums.CouplingTypeA)
		self._core.io.write(f'INPut:COUPling {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CouplingTypeA:
		"""SCPI: INPut:COUPling \n
		Snippet: value: enums.CouplingTypeA = driver.applications.k70Vsa.inputPy.coupling.get() \n
		Selects the coupling type of the RF input. The command is not available for measurements with the optional 'Digital
		Baseband' interface. If an external frontend is active, the coupling is automatically set to AC. \n
			:return: input_coupling: No help available"""
		response = self._core.io.query_str(f'INPut:COUPling?')
		return Conversions.str_to_scalar_enum(response, enums.CouplingTypeA)
