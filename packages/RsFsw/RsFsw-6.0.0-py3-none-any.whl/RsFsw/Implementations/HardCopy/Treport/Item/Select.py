from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelectCls:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, item: str, arg_1: str = None) -> None:
		"""SCPI: HCOPy:TREPort:ITEM:SELect \n
		Snippet: driver.hardCopy.treport.item.select.set(item = rawAbc, arg_1 = 'abc') \n
		This command defines the type of information that a test report consists of. \n
			:param item: String containing the information you want to include in the test report. Note that the items, separated by commas, have to be written into one string (see example below) . The available items depend on the application you are using. See the tables below for a short description of each item. By default, some items are selected (see tables below) .
			:param arg_1: Optional parameter to define the channel type that the selection applies to. When you omit the ChannelType parameter, the selection applies to the currently active channel.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('item', item, DataType.RawString), ArgSingle('arg_1', arg_1, DataType.String, None, is_optional=True))
		self._core.io.write(f'HCOPy:TREPort:ITEM:SELect {param}'.rstrip())
