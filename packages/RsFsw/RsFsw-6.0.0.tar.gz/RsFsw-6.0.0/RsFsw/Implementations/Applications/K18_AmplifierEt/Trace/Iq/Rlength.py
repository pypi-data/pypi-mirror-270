from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RlengthCls:
	"""Rlength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rlength", core, parent)

	def get(self) -> float:
		"""SCPI: TRACe:IQ:RLENgth \n
		Snippet: value: float = driver.applications.k18AmplifierEt.trace.iq.rlength.get() \n
		Sets the record length for the acquired I/Q data. Increasing the record length also increases the measurement time. Note:
		Alternatively, you can define the measurement time using the SENS:SWE:TIME command. \n
			:return: samples: No help available"""
		response = self._core.io.query_str(f'TRACe:IQ:RLENgth?')
		return Conversions.str_to_float(response)
