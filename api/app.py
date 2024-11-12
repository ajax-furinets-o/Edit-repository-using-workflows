from fastapi import FastAPI, Depends

from src.adapter.github.dispatcher import GitHubDispatcher
from src.model.feature import FeatureEpicT
from src.service.feature_service import FeatureService

app = FastAPI()


def dependency_container() -> FeatureService:
    dispatcher = GitHubDispatcher()
    service = FeatureService(dispatcher=dispatcher)
    yield service


@app.post("/feature/epic")
async def edit_feature_epic(
        epic: FeatureEpicT,
        service: FeatureService = Depends(dependency_container),
):
    return await service.edit_epic(epic=epic)
