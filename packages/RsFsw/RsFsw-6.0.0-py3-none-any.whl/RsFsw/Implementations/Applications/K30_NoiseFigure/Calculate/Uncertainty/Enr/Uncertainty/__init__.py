from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UncertaintyCls:
	"""Uncertainty commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uncertainty", core, parent)

	@property
	def hot(self):
		"""hot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hot'):
			from .Hot import HotCls
			self._hot = HotCls(self._core, self._cmd_group)
		return self._hot

	@property
	def cold(self):
		"""cold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cold'):
			from .Cold import ColdCls
			self._cold = ColdCls(self._core, self._cmd_group)
		return self._cold

	def set(self, uncertainty: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNCertainty:ENR:UNCertainty \n
		Snippet: driver.applications.k30NoiseFigure.calculate.uncertainty.enr.uncertainty.set(uncertainty = 1.0, window = repcap.Window.Default) \n
		Defines the uncertainty of a noise source. If the noise sources during calibration and measurement are different, the
		command defines the uncertainty of the measurement noise source. If a smart noise source is used, the uncertainty values
		defined in the SNS table are used. \n
			:param uncertainty: Uncertainty value of the noise source. Refer to the specifications document of the noise source to determine its uncertainty. Unit: DB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(uncertainty)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNCertainty:ENR:UNCertainty {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:UNCertainty:ENR:UNCertainty \n
		Snippet: value: float = driver.applications.k30NoiseFigure.calculate.uncertainty.enr.uncertainty.get(window = repcap.Window.Default) \n
		Defines the uncertainty of a noise source. If the noise sources during calibration and measurement are different, the
		command defines the uncertainty of the measurement noise source. If a smart noise source is used, the uncertainty values
		defined in the SNS table are used. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: uncertainty: Uncertainty value of the noise source. Refer to the specifications document of the noise source to determine its uncertainty. Unit: DB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNCertainty:ENR:UNCertainty?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'UncertaintyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UncertaintyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
