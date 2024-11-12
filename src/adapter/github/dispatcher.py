from src.model.feature import FeatureEpicT
from src.service.dependencies import Dispatcher


class GitHubDispatcher(Dispatcher):

    async def edit_epic(self, epic: FeatureEpicT) -> str:
        pass
