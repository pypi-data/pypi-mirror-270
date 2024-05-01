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

	def set(self, coupling_type: enums.CouplingTypeA) -> None:
		"""SCPI: INPut:COUPling \n
		Snippet: driver.applications.k50Spurious.inputPy.coupling.set(coupling_type = enums.CouplingTypeA.AC) \n
		Selects the coupling type of the RF input. The command is not available for measurements with the optional 'Digital
		Baseband' interface. If an external frontend is active, the coupling is automatically set to AC. \n
			:param coupling_type: AC | DC AC AC coupling DC DC coupling
		"""
		param = Conversions.enum_scalar_to_str(coupling_type, enums.CouplingTypeA)
		self._core.io.write(f'INPut:COUPling {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CouplingTypeA:
		"""SCPI: INPut:COUPling \n
		Snippet: value: enums.CouplingTypeA = driver.applications.k50Spurious.inputPy.coupling.get() \n
		Selects the coupling type of the RF input. The command is not available for measurements with the optional 'Digital
		Baseband' interface. If an external frontend is active, the coupling is automatically set to AC. \n
			:return: coupling_type: AC | DC AC AC coupling DC DC coupling"""
		response = self._core.io.query_str(f'INPut:COUPling?')
		return Conversions.str_to_scalar_enum(response, enums.CouplingTypeA)
