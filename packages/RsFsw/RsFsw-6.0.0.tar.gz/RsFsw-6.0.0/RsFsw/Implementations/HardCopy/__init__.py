from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HardCopyCls:
	"""HardCopy commands group definition. 60 total commands, 15 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hardCopy", core, parent)

	@property
	def cmap(self):
		"""cmap commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmap'):
			from .Cmap import CmapCls
			self._cmap = CmapCls(self._core, self._cmd_group)
		return self._cmap

	@property
	def device(self):
		"""device commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_device'):
			from .Device import DeviceCls
			self._device = DeviceCls(self._core, self._cmd_group)
		return self._device

	@property
	def print(self):
		"""print commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_print'):
			from .Print import PrintCls
			self._print = PrintCls(self._core, self._cmd_group)
		return self._print

	@property
	def destination(self):
		"""destination commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_destination'):
			from .Destination import DestinationCls
			self._destination = DestinationCls(self._core, self._cmd_group)
		return self._destination

	@property
	def immediate(self):
		"""immediate commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_immediate'):
			from .Immediate import ImmediateCls
			self._immediate = ImmediateCls(self._core, self._cmd_group)
		return self._immediate

	@property
	def item(self):
		"""item commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_item'):
			from .Item import ItemCls
			self._item = ItemCls(self._core, self._cmd_group)
		return self._item

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	@property
	def tdDtamp(self):
		"""tdDtamp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdDtamp'):
			from .TdDtamp import TdDtampCls
			self._tdDtamp = TdDtampCls(self._core, self._cmd_group)
		return self._tdDtamp

	@property
	def page(self):
		"""page commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_page'):
			from .Page import PageCls
			self._page = PageCls(self._core, self._cmd_group)
		return self._page

	@property
	def content(self):
		"""content commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_content'):
			from .Content import ContentCls
			self._content = ContentCls(self._core, self._cmd_group)
		return self._content

	@property
	def copies(self):
		"""copies commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_copies'):
			from .Copies import CopiesCls
			self._copies = CopiesCls(self._core, self._cmd_group)
		return self._copies

	@property
	def comment(self):
		"""comment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_comment'):
			from .Comment import CommentCls
			self._comment = CommentCls(self._core, self._cmd_group)
		return self._comment

	@property
	def logo(self):
		"""logo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_logo'):
			from .Logo import LogoCls
			self._logo = LogoCls(self._core, self._cmd_group)
		return self._logo

	@property
	def treport(self):
		"""treport commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_treport'):
			from .Treport import TreportCls
			self._treport = TreportCls(self._core, self._cmd_group)
		return self._treport

	@property
	def theme(self):
		"""theme commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_theme'):
			from .Theme import ThemeCls
			self._theme = ThemeCls(self._core, self._cmd_group)
		return self._theme

	def abort(self) -> None:
		"""SCPI: HCOPy:ABORt \n
		Snippet: driver.hardCopy.abort() \n
		This command aborts a running hardcopy output. \n
		"""
		self._core.io.write(f'HCOPy:ABORt')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: HCOPy:ABORt \n
		Snippet: driver.hardCopy.abort_with_opc() \n
		This command aborts a running hardcopy output. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'HCOPy:ABORt', opc_timeout_ms)

	def clone(self) -> 'HardCopyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HardCopyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
