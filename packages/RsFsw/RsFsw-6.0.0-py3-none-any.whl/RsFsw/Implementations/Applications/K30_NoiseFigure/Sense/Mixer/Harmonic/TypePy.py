from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, odd_even: enums.OddEven) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic:TYPE \n
		Snippet: driver.applications.k30NoiseFigure.sense.mixer.harmonic.typePy.set(odd_even = enums.OddEven.EODD) \n
		Specifies whether the harmonic order to be used should be odd, even, or both. Which harmonics are supported depends on
		the mixer type. \n
			:param odd_even: ODD | EVEN | EODD ODD | EVEN | EODD
		"""
		param = Conversions.enum_scalar_to_str(odd_even, enums.OddEven)
		self._core.io.write(f'SENSe:MIXer:HARMonic:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.OddEven:
		"""SCPI: [SENSe]:MIXer:HARMonic:TYPE \n
		Snippet: value: enums.OddEven = driver.applications.k30NoiseFigure.sense.mixer.harmonic.typePy.get() \n
		Specifies whether the harmonic order to be used should be odd, even, or both. Which harmonics are supported depends on
		the mixer type. \n
			:return: odd_even: ODD | EVEN | EODD ODD | EVEN | EODD"""
		response = self._core.io.query_str(f'SENSe:MIXer:HARMonic:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.OddEven)
