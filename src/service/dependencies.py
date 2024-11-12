import abc

from src.model.feature import FeatureEpicT


class Dispatcher(abc.ABC):

    @abc.abstractmethod
    async def edit_epic(self, epic: FeatureEpicT) -> str:
        ...
