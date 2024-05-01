from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UnitCls:
	"""Unit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	def set(self, full_scale_level_unit: enums.FullScaleLevelUnit) -> None:
		"""SCPI: INPut:DIQ:RANGe[:UPPer]:UNIT \n
		Snippet: driver.applications.k70Vsa.inputPy.diq.range.upper.unit.set(full_scale_level_unit = enums.FullScaleLevelUnit.DBM) \n
		Defines the unit of the full scale level. The availability of units depends on the measurement application you are using.
		Is only available if the optional 'Digital Baseband' interface is installed. \n
			:param full_scale_level_unit: DBM | DBPW | WATT | DBUV | DBMV | VOLT | DBUA | AMPere
		"""
		param = Conversions.enum_scalar_to_str(full_scale_level_unit, enums.FullScaleLevelUnit)
		self._core.io.write(f'INPut:DIQ:RANGe:UPPer:UNIT {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FullScaleLevelUnit:
		"""SCPI: INPut:DIQ:RANGe[:UPPer]:UNIT \n
		Snippet: value: enums.FullScaleLevelUnit = driver.applications.k70Vsa.inputPy.diq.range.upper.unit.get() \n
		Defines the unit of the full scale level. The availability of units depends on the measurement application you are using.
		Is only available if the optional 'Digital Baseband' interface is installed. \n
			:return: full_scale_level_unit: No help available"""
		response = self._core.io.query_str(f'INPut:DIQ:RANGe:UPPer:UNIT?')
		return Conversions.str_to_scalar_enum(response, enums.FullScaleLevelUnit)
