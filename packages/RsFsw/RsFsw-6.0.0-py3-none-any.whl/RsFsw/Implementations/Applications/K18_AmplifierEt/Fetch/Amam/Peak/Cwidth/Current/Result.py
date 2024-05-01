from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:AMAM:PEAK:CWIDth:CURRent[:RESult] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.amam.peak.cwidth.current.result.get() \n
		This command queries the 'AM/AM' peak curve width as shown in the result summary. \n
			:return: curve_width: numeric value Current 'AM/AM' peak curve width. Unit: dB"""
		response = self._core.io.query_str(f'FETCh:AMAM:PEAK:CWIDth:CURRent:RESult?')
		return Conversions.str_to_float(response)
