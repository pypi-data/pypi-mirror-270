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
		"""SCPI: FETCh:PTABle:CFACtor:MAXimum:X[:RESult] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.ptable.cfactor.maximum.x.result.get() \n
		These commands query the x-axis value at which the maximum result value for the parameter was determined, as shown in the
		'Parameter Sweep' table. For details on the parameters, see 'Amplifier parameters'. \n
			:return: results: numeric value The value depends on the parameter selected for the x-axis (see method RsFsw.Applications.K18_AmplifierEt.Configure.Psweep.X.Setting.set) ."""
		response = self._core.io.query_str(f'FETCh:PTABle:CFACtor:MAXimum:X:RESult?')
		return Conversions.str_to_float(response)
