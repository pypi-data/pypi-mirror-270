from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdeviceCls:
	"""Cdevice commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdevice", core, parent)

	def get(self) -> str:
		"""SCPI: INPut:DIQ:CDEVice \n
		Snippet: value: str = driver.applications.k6Pulse.inputPy.diq.cdevice.get() \n
		Queries the current configuration and the status of the digital I/Q input from the optional 'Digital Baseband' interface.
		For details see 'Interface Status Information'. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'INPut:DIQ:CDEVice?')
		return trim_str_response(response)
