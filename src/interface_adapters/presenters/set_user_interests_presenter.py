from dataclasses import dataclass


@dataclass
class SetInterestsResponseDto:
    success: bool
    message: str


class SetUserInterestsPresenter:
    def present_success(self) -> SetInterestsResponseDto:
        return SetInterestsResponseDto(success=True, message="Interests saved")

    def present_failure(self, msg: str) -> SetInterestsResponseDto:
        return SetInterestsResponseDto(success=False, message=msg)
