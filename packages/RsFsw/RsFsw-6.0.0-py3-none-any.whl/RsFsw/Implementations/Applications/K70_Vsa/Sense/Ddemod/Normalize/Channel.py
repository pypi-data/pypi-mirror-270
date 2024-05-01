from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChannelCls:
	"""Channel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("channel", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:NORMalize:CHANnel \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.normalize.channel.set(state = False) \n
		Switches the channel compensation on or off. (With equalizer only) \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:NORMalize:CHANnel {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:NORMalize:CHANnel \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.normalize.channel.get() \n
		Switches the channel compensation on or off. (With equalizer only) \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:DDEMod:NORMalize:CHANnel?')
		return Conversions.str_to_bool(response)
