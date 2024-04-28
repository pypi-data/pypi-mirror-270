import re
from typing import Optional, List
from ..common_check import CommonCheck


class MypyRunner(CommonCheck):
    def _build_command(self, target: str) -> str:
        command: str = self.get_executable()
        if self.has_config:
            command += f" --config-file {self.config_path}"
        command += f" {target}"
        return command

    RATING_PATTERN: re.Pattern = re.compile(r".*?([\d\.\/]+)")

    def __init__(self, bound: str = "<15", configuration_path: Optional[str] = None,
                 executable_path: Optional[str] = None) -> None:
        CommonCheck.__init__(self, name="mypy", bound=bound, configuration_path=configuration_path,
                             executable_path=executable_path)

    def _calculate_score(self, ret, lines: List[str]) -> float:
        from ...enforcers import exit_if
        rating_line = lines[-1]
        exit_if(not (m := self.RATING_PATTERN.match(rating_line)),
                f"Failed running MyPy, got exit code {ret}. try running manually using:\n\t{self._build_command('TARGE')}")
        rating_string = m.group(1)
        return float(rating_string)


__all__ = [
    'MypyRunner',
]
