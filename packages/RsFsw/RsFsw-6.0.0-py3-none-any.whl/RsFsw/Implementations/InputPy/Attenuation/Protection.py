from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ProtectionCls:
	"""Protection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("protection", core, parent)

	def reset(self, device_name: str = None) -> None:
		"""SCPI: INPut:ATTenuation:PROTection:RESet \n
		Snippet: driver.inputPy.attenuation.protection.reset(device_name = 'abc') \n
		Resets the attenuator and reconnects the RF input with the input mixer for the FSW after an overload condition occurred
		and the protection mechanism intervened. The error status bit (bit 3 in the method RsFsw.Status.Questionable.Power.Event.
		get_ status register) and the INPUT OVLD message in the status bar are cleared. (See method RsFsw.Status.Questionable.
		Power.Event.get_ and 'STATus:QUEStionable:POWer register') . The command works only if the overload condition has been
		eliminated first. For details on the protection mechanism, see 'RF Input Protection'. \n
			:param device_name: No help available
		"""
		param = ''
		if device_name:
			param = Conversions.value_to_quoted_str(device_name)
		self._core.io.write(f'INPut:ATTenuation:PROTection:RESet {param}'.strip())
