from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReferenceCls:
	"""Reference commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	def set(self, arg_0: enums.DdemodFilter) -> None:
		"""SCPI: [SENSe]:DDEMod:FILTer:REFerence \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.filterPy.reference.set(arg_0 = enums.DdemodFilter.A25Fm) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.enum_scalar_to_str(arg_0, enums.DdemodFilter)
		self._core.io.write(f'SENSe:DDEMod:FILTer:REFerence {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DdemodFilter:
		"""SCPI: [SENSe]:DDEMod:FILTer:REFerence \n
		Snippet: value: enums.DdemodFilter = driver.applications.k70Vsa.sense.ddemod.filterPy.reference.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:FILTer:REFerence?')
		return Conversions.str_to_scalar_enum(response, enums.DdemodFilter)
