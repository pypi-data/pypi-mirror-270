from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandwidthCls:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def get(self) -> float:
		"""SCPI: TRACe:IQ:BWIDth \n
		Snippet: value: float = driver.applications.k149Uwb.trace.iq.bandwidth.get() \n
		Defines or queries the bandwidth of the resampling filter. The bandwidth of the resampling filter depends on the sample
		rate. \n
			:return: bandwidth: Unit: HZ"""
		response = self._core.io.query_str(f'TRACe:IQ:BWIDth?')
		return Conversions.str_to_float(response)
