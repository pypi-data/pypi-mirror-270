from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def get(self) -> float:
		"""SCPI: CONFigure:DDPD:RMS[:CURRent] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.ddpd.rms.current.get() \n
		Returns the current RMS power level in manual direct DPD mode. \n
			:return: level: numeric value"""
		response = self._core.io.query_str(f'CONFigure:DDPD:RMS:CURRent?')
		return Conversions.str_to_float(response)
