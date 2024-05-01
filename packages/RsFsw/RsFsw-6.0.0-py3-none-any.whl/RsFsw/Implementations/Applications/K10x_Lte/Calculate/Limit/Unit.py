from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UnitCls:
	"""Unit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	def set(self, unit: enums.LimitUnitB, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:UNIT \n
		Snippet: driver.applications.k10Xlte.calculate.limit.unit.set(unit = enums.LimitUnitB.AMPere, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Defines the unit of a limit line. \n
			:param unit: DBM | DBPW | WATT | DBUV | DBMV | VOLT | DBUA | AMPere | DB | DBUV_M | DBUA_M | DBM_hz | DBM_mhz | DBUV_mhz | DBMV_mhz | DBUa_mhz | DBUV_m | DBUa_m | DBUV_mmhz | DBUa_mmhz | DBPW_mhz | DBPT_mhz | DBPT | (unitless) If you select a dB-based unit for the limit line, the command automatically turns the limit line into a relative limit line.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.LimitUnitB)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:UNIT {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> enums.LimitUnitB:
		"""SCPI: CALCulate<n>:LIMit<li>:UNIT \n
		Snippet: value: enums.LimitUnitB = driver.applications.k10Xlte.calculate.limit.unit.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Defines the unit of a limit line. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: unit: DBM | DBPW | WATT | DBUV | DBMV | VOLT | DBUA | AMPere | DB | DBUV_M | DBUA_M | DBM_hz | DBM_mhz | DBUV_mhz | DBMV_mhz | DBUa_mhz | DBUV_m | DBUa_m | DBUV_mmhz | DBUa_mmhz | DBPW_mhz | DBPT_mhz | DBPT | (unitless) If you select a dB-based unit for the limit line, the command automatically turns the limit line into a relative limit line."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:UNIT?')
		return Conversions.str_to_scalar_enum(response, enums.LimitUnitB)
