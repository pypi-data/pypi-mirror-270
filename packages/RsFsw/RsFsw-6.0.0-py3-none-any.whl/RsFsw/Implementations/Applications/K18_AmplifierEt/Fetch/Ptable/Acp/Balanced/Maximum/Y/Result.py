from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:PTABle:ACP:BALanced:MAXimum:Y[:RESult] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.ptable.acp.balanced.maximum.y.result.get() \n
		These commands query the y-axis value at which the maximum result value for the parameter was determined, as shown in the
		'Parameter Sweep' table. For details on the parameters, see 'Amplifier parameters'. \n
			:return: results: numeric value The value depends on the parameter selected for the y-axis (see method RsFsw.Applications.K18_AmplifierEt.Configure.Psweep.Y.Setting.set) ."""
		response = self._core.io.query_str(f'FETCh:PTABle:ACP:BALanced:MAXimum:Y:RESult?')
		return Conversions.str_to_float(response)
