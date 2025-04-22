from dataclasses import dataclass
from dataclasses import asdict


@dataclass
class SetInterestsResponseDto:
    success: bool
    message: str


class SetUserInterestsPresenter:
    def present_success(self) -> SetInterestsResponseDto:
        return asdict(SetInterestsResponseDto(success=True, message="Interests saved"))

    def present_failure(self, msg: str) -> SetInterestsResponseDto:
        return asdict(SetInterestsResponseDto(success=False, message=msg))
