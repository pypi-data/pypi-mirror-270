from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CommentCls:
	"""Comment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("comment", core, parent)

	def set(self, comment: str) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:COMMent \n
		Snippet: driver.applications.k50Spurious.sense.correction.cvl.comment.set(comment = 'abc') \n
		Defines a comment for the conversion loss table. Before this command can be performed, the conversion loss table must be
		selected (see [SENSe:]CORRection:CVL:SELect) . Is only available with option B21 (External Mixer) installed. \n
			:param comment: No help available
		"""
		param = Conversions.value_to_quoted_str(comment)
		self._core.io.write(f'SENSe:CORRection:CVL:COMMent {param}')

	def get(self, comment: str) -> str:
		"""SCPI: [SENSe]:CORRection:CVL:COMMent \n
		Snippet: value: str = driver.applications.k50Spurious.sense.correction.cvl.comment.get(comment = 'abc') \n
		Defines a comment for the conversion loss table. Before this command can be performed, the conversion loss table must be
		selected (see [SENSe:]CORRection:CVL:SELect) . Is only available with option B21 (External Mixer) installed. \n
			:param comment: No help available
			:return: comment: No help available"""
		param = Conversions.value_to_quoted_str(comment)
		response = self._core.io.query_str(f'SENSe:CORRection:CVL:COMMent? {param}')
		return trim_str_response(response)
