from src.model.feature import FeatureEpicT
from src.service.dependencies import Dispatcher


class FeatureService:

    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher = dispatcher

    async def edit_epic(self, epic: FeatureEpicT):
        return await self.dispatcher.edit_epic(epic=epic)