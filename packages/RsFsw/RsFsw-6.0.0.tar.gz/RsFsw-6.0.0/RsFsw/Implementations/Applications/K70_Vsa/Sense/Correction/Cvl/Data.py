from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, data: float) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:DATA \n
		Snippet: driver.applications.k70Vsa.sense.correction.cvl.data.set(data = 1.0) \n
		Defines the reference values of the selected conversion loss tables. The values are entered as a set of frequency/level
		pairs. You can define a maximum of 500 frequency/level pairs. Before this command can be performed, you must select the
		conversion loss table (see [SENSe:]CORRection:CVL:SELect) . Is only available with option B21 (External Mixer) installed. \n
			:param data: No help available
		"""
		param = Conversions.decimal_value_to_str(data)
		self._core.io.write(f'SENSe:CORRection:CVL:DATA {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:CVL:DATA \n
		Snippet: value: float = driver.applications.k70Vsa.sense.correction.cvl.data.get() \n
		Defines the reference values of the selected conversion loss tables. The values are entered as a set of frequency/level
		pairs. You can define a maximum of 500 frequency/level pairs. Before this command can be performed, you must select the
		conversion loss table (see [SENSe:]CORRection:CVL:SELect) . Is only available with option B21 (External Mixer) installed. \n
			:return: data: No help available"""
		response = self._core.io.query_str(f'SENSe:CORRection:CVL:DATA?')
		return Conversions.str_to_float(response)
