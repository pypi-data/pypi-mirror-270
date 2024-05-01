from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.Utilities import trim_str_response
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Absolute import AbsoluteCls
			self._absolute = AbsoluteCls(self._core, self._cmd_group)
		return self._absolute

	@property
	def relative(self):
		"""relative commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relative'):
			from .Relative import RelativeCls
			self._relative = RelativeCls(self._core, self._cmd_group)
		return self._relative

	def get(self, result: enums.AcpResult = None, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> str:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:ALTernate:RESult \n
		Snippet: value: str = driver.applications.k10Xlte.calculate.limit.acPower.alternate.result.get(result = enums.AcpResult.ABSolute, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Queries the limit check results for the alternate channels during ACLR measurements. \n
			:param result: REL Queries the channel power limit check results. ABS Queries the distance to the limit line.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: limit_check: Returns two values, one for the upper and one for the lower alternate channel. PASSED Limit check has passed. FAILED Limit check has failed."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('result', result, DataType.Enum, enums.AcpResult, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:ALTernate:RESult? {param}'.rstrip())
		return trim_str_response(response)

	def clone(self) -> 'ResultCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResultCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
