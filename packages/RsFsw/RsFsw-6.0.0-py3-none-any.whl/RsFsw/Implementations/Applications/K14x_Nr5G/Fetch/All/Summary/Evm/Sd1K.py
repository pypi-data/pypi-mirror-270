from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sd1KCls:
	"""Sd1K commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sd1K", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:ALL:SUMMary:EVM:SD1K \n
		Snippet: value: float = driver.applications.k14Xnr5G.fetch.all.summary.evm.sd1K.get() \n
		Queries the EVM of all PUSCH DMRS resource elements with a QPSK modulation.
			INTRO_CMD_HELP: method RsFsw.Applications.K14x_Nr5G.Fetch.All.Summary.Evm.Sdqp.get_ queries the average result over all carriers. Prerequisites: \n
			- Select to evaluate all carriers ([SENSe:]NR5G:RSUMmary:CCResult) . \n
			:return: evm: EVM in % or dB."""
		response = self._core.io.query_str(f'FETCh:ALL:SUMMary:EVM:SD1K?')
		return Conversions.str_to_float(response)
