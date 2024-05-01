from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UpperCls:
	"""Upper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upper", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: INPut:DIQ:RANGe[:UPPer] \n
		Snippet: driver.applications.k91Wlan.inputPy.diq.range.upper.set(level = 1.0) \n
		Defines or queries the 'Full Scale Level', i.e. the level that corresponds to an I/Q sample with the magnitude '1'.
		Is only available if the optional 'Digital Baseband' interface is installed. \n
			:param level: Range: 1 uV to 7.071 V, Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'INPut:DIQ:RANGe:UPPer {param}')

	def get(self) -> float:
		"""SCPI: INPut:DIQ:RANGe[:UPPer] \n
		Snippet: value: float = driver.applications.k91Wlan.inputPy.diq.range.upper.get() \n
		Defines or queries the 'Full Scale Level', i.e. the level that corresponds to an I/Q sample with the magnitude '1'.
		Is only available if the optional 'Digital Baseband' interface is installed. \n
			:return: level: Range: 1 uV to 7.071 V, Unit: DBM"""
		response = self._core.io.query_str(f'INPut:DIQ:RANGe:UPPer?')
		return Conversions.str_to_float(response)
