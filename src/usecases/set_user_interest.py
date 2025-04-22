from interface_adapters.dtos.users import UserInterestInputDto
from interface_adapters.repositories_interfaces.user_interest_repo import UserInterestRepository
from interface_adapters.presenters.set_user_interests_presenter import SetUserInterestsPresenter


class SetUserInterestsUseCase:
    def __init__(self, repo: UserInterestRepository, presenter: SetUserInterestsPresenter):
        self.repo = repo
        self.presenter = presenter

    def execute(self, data: UserInterestInputDto):
        try:
            self.repo.set_interests_for_user(data.user_id, data.interests)
            return self.presenter.present_success()
        except Exception as e:
            return self.presenter.present_failure(str(e))
