from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SbandCls:
	"""Sband commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sband", core, parent)

	def get(self) -> float:
		"""SCPI: OUTPut:IF:SBANd \n
		Snippet: value: float = driver.output.ifreq.sband.get() \n
		Queries the sideband provided at the 'IF OUT 2 GHz' connector compared to the sideband of the RF signal. The sideband
		depends on the current center frequency. Is available only if the output is configured for IF2 (see method RsFsw.Output.
		Ifreq.Source.set) . For more information and prerequisites see 'IF and video signal output'. \n
			:return: side_band: NORMal The sideband at the output is identical to the RF signal. INVerted The sideband at the output is the inverted RF signal sideband."""
		response = self._core.io.query_str(f'OUTPut:IF:SBANd?')
		return Conversions.str_to_float(response)
