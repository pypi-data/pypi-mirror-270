from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqMcompCls:
	"""IqMcomp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqMcomp", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:TRACking:IQMComp \n
		Snippet: driver.applications.k91Wlan.sense.tracking.iqMcomp.set(state = False) \n
		Activates or deactivates the compensation for I/Q mismatch (gain imbalance, quadrature offset, I/Q skew, see 'I/Q
		mismatch') . This setting is not available for standards IEEE 802.11b and g (DSSS) . \n
			:param state: ON | 1 | AVGScarrier The I/Q mismatches (gain imbalance, quadrature offset, time skew) are averaged over the subcarriers. The scalar results are applied to the subcarriers and used for I/Q mismatch compensation. PERScarrier The individual I/Q mismatches per subcarrier are used for I/Q mismatch compensation. OFF | 0 Compensation is not applied; this setting is required for measurements strictly according to the IEEE 802.11-2012, IEEE 802.11ac-2013 WLAN standard
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:TRACking:IQMComp {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:TRACking:IQMComp \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.tracking.iqMcomp.get() \n
		Activates or deactivates the compensation for I/Q mismatch (gain imbalance, quadrature offset, I/Q skew, see 'I/Q
		mismatch') . This setting is not available for standards IEEE 802.11b and g (DSSS) . \n
			:return: state: ON | 1 | AVGScarrier The I/Q mismatches (gain imbalance, quadrature offset, time skew) are averaged over the subcarriers. The scalar results are applied to the subcarriers and used for I/Q mismatch compensation. PERScarrier The individual I/Q mismatches per subcarrier are used for I/Q mismatch compensation. OFF | 0 Compensation is not applied; this setting is required for measurements strictly according to the IEEE 802.11-2012, IEEE 802.11ac-2013 WLAN standard"""
		response = self._core.io.query_str(f'SENSe:TRACking:IQMComp?')
		return Conversions.str_to_bool(response)
