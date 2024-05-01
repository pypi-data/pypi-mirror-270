from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AttenuationCls:
	"""Attenuation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	def set(self, attenuation: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:INPut:ATTenuation \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.inputPy.attenuation.set(attenuation = 1.0, rangePy = repcap.RangePy.Default) \n
		Defines the input attenuation for a spurious emission measurement range. The sweep list cannot be configured using remote
		commands during an on-going sweep operation. \n
			:param attenuation: Numeric value. Refer to the specifications document for the attenuation range. Unit: dB
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:INPut:ATTenuation {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:INPut:ATTenuation \n
		Snippet: value: float = driver.applications.k50Spurious.sense.listPy.range.inputPy.attenuation.get(rangePy = repcap.RangePy.Default) \n
		Defines the input attenuation for a spurious emission measurement range. The sweep list cannot be configured using remote
		commands during an on-going sweep operation. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: attenuation: Numeric value. Refer to the specifications document for the attenuation range. Unit: dB"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:INPut:ATTenuation?')
		return Conversions.str_to_float(response)
