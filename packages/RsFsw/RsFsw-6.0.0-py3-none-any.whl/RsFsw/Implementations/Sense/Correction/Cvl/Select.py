from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelectCls:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:SELect \n
		Snippet: driver.sense.correction.cvl.select.set(filename = 'abc') \n
		Selects the conversion loss table with the specified file name. If <file_name> is not available, a new conversion loss
		table is created. Is only available with option B21 (External Mixer) installed. \n
			:param filename: String containing the path and name of the file.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:CORRection:CVL:SELect {param}')
