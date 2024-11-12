from src.adapter.github.http import GitHubHttpClient
from src.model.feature import FeatureEpicT
from src.service.dependencies import Dispatcher


class GitHubDispatcher(Dispatcher):

    def __init__(self, transport: GitHubHttpClient):
        self.transport = transport

    async def edit_epic(self, epic: FeatureEpicT) -> str:
        pass