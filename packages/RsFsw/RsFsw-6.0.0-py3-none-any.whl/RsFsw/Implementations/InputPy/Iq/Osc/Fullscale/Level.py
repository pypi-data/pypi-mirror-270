from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelCls:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: INPut:IQ:OSC:FULLscale[:LEVel] \n
		Snippet: driver.inputPy.iq.osc.fullscale.level.set(level = 1.0) \n
		The full scale level defines the maximum power for baseband input possible without clipping the signal. For manual input,
		this setting corresponds to the setting on the oscilloscope. Thus, possible scaling values of the oscilloscope are
		allowed. \n
			:param level: Unit: V
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'INPut:IQ:OSC:FULLscale:LEVel {param}')

	def get(self) -> float:
		"""SCPI: INPut:IQ:OSC:FULLscale[:LEVel] \n
		Snippet: value: float = driver.inputPy.iq.osc.fullscale.level.get() \n
		The full scale level defines the maximum power for baseband input possible without clipping the signal. For manual input,
		this setting corresponds to the setting on the oscilloscope. Thus, possible scaling values of the oscilloscope are
		allowed. \n
			:return: level: Unit: V"""
		response = self._core.io.query_str(f'INPut:IQ:OSC:FULLscale:LEVel?')
		return Conversions.str_to_float(response)
