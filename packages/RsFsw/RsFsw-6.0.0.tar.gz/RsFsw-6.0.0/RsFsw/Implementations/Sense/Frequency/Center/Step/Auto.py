from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP:AUTO \n
		Snippet: driver.sense.frequency.center.step.auto.set(state = False) \n
		Couples or decouples the center frequency step size to the span. In time domain (zero span) measurements, the center
		frequency is coupled to the RBW. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:FREQuency:CENTer:STEP:AUTO {param}')
