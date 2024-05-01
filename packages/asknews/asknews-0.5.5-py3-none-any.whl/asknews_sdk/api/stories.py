from asknews_sdk.api.base import BaseAPI
from asknews_sdk.dto.stories import (
    StoriesResponse,
    StoryResponse
)
from typing import Literal
from uuid import UUID

class StoriesAPI(BaseAPI):
    """
    Stories API

    https://docs.asknews.app/en/reference#tag--stories
    """
    def search_stories(
        self,
        query: str | None = None,
        categories: list[
            Literal[
                "Politics",
                "Economy",
                "Finance",
                "Science",
                "Technology",
                "Sports",
                "Climate",
                "Environment",
                "Culture",
                "Entertainment",
                "Business",
                "Health",
                "International"
            ]
        ] = [],
        uuids: list[UUID] = [],
        start_timestamp: int | None = None,
        end_timestamp: int | None = None,
        sort_by: Literal[
            "published", "coverage", "sentiment", "confidence", "relevance"
        ] | None = None,
        sort_type: Literal["asc", "desc"] | None = None,
        continent: Literal[
            "Africa",
            "Asia",
            "Europe",
            "Middle East",
            "North America",
            "South America",
            "Oceania",
        ] | None = None,
        offset: int | str | None = None,
        limit: int = 50,
        expand_updates: bool = False,
        max_updates: int = 11,
        max_articles: int = 5,
        reddit: int = 0,
        method: Literal["nl", "kw", "both"] = "kw",
        obj_type: list[Literal["story", "story_update"]] = ["story"]
    ) -> StoriesResponse:
        """
        Get the news stories.

        https://docs.asknews.app/en/reference#get-/v1/stories

        :param query: The query.
        :type query: str | None
        :param categories: The categories.
        :type categories: str | None
        :param start_timestamp: The start timestamp.
        :type start_timestamp: int | None
        :param end_timestamp: The end timestamp.
        :type end_timestamp: int | None
        :param sort_by_time: Whether to sort by time.
        :type sort_by_time: bool
        :param continent: The continent to filter by.
        :type continent: str | None
        :param offset: The offset.
        :type offset: int
        :param limit: The limit.
        :type limit: int
        :param expand_updates: Whether to expand updates.
        :type expand_updates: bool
        :param max_updates: The max updates per story.
        :type max_updates: int
        :param max_articles: The max articles per update.
        :type max_articles: int
        :param reddit: Amount of reddit threads to include per update.
        :type reddit: int
        :param method: The method to use for searching.
        :type method: str
        :param obj_type: The object type to filter on.
        :type obj_type: list[str]
        :return: The stories response.
        :rtype: StoriesResponse
        """
        response = self.client.request(
            method="GET",
            endpoint="/v1/stories",
            query={
                "query": query,
                "categories": categories,
                "start_timestamp": start_timestamp,
                "end_timestamp": end_timestamp,
                "offset": offset,
                "method": method,
                "sort_by": sort_by,
                "sort_type": sort_type,
                "continent": continent,
                "obj_type": obj_type,
                "reddit": reddit,
                "limit": limit,
                "expand_updates": expand_updates,
                "max_updates": max_updates,
                "max_articles": max_articles,
                "uuids": uuids
            },
            accept=[(StoriesResponse.__content_type__, 1.0)]
        )

        return StoriesResponse.model_validate(response.content)

    def get_story(
        self,
        story_id: UUID | str,
        expand_updates: bool = True,
        max_updates: int = 11,
        max_articles: int = 5,
        reddit: int = 0,
    ) -> StoryResponse:
        """
        Get a single news story given the ID.

        https://docs.asknews.app/en/reference#get-/v1/stories/-story_id-

        :param story_id: The story ID or URL safe title.
        :type story_id: str
        :param expand_updates: Whether to expand updates.
        :type expand_updates: bool
        :param max_updates: The max updates per story.
        :type max_updates: int
        :param max_articles: The max articles per update.
        :type max_articles: int
        :param reddit: Amount of reddit threads to include per update.
        :type reddit: int
        :return: The story response.
        :rtype: StoryResponse
        """
        response = self.client.request(
            method="GET",
            endpoint="/v1/stories/{story_id}",
            query={
                "expand_updates": expand_updates,
                "max_updates": max_updates,
                "max_articles": max_articles,
                "reddit": reddit
            },
            params={"story_id": story_id},
            accept=[(StoryResponse.__content_type__, 1.0)]
        )
        return StoryResponse.model_validate(response.content)


class AsyncStoriesAPI(BaseAPI):
    """
    Stories API

    https://docs.asknews.app/en/reference#tag--stories
    """
    async def search_stories(
        self,
        query: str | None = None,
        categories: list[
            Literal[
                "Politics",
                "Economy",
                "Finance",
                "Science",
                "Technology",
                "Sports",
                "Climate",
                "Environment",
                "Culture",
                "Entertainment",
                "Business",
                "Health",
                "International"
            ]
        ] = [],
        uuids: list[UUID] = [],
        start_timestamp: int | None = None,
        end_timestamp: int | None = None,
        sort_by: Literal[
            "published", "coverage", "sentiment", "relevance", "confidence"
        ] | None = None,
        sort_type: Literal["asc", "desc"] | None = None,
        continent: Literal[
            "Africa",
            "Asia",
            "Europe",
            "Middle East",
            "North America",
            "South America",
            "Oceania",
        ] | None = None,
        offset: int | str | None = None,
        limit: int = 50,
        expand_updates: bool = False,
        max_updates: int = 11,
        max_articles: int = 5,
        reddit: int = 0,
        method: Literal["nl", "kw", "both"] = "kw",
        obj_type: list[
            Literal["story", "story_update"]
        ] = ["story"]
    ) -> StoriesResponse:
        """
        Get the news stories.

        https://docs.asknews.app/en/reference#get-/v1/stories

        :param query: The query.
        :type query: str | None
        :param categories: The categories.
        :type categories: str | None
        :param start_timestamp: The start timestamp.
        :type start_timestamp: int | None
        :param end_timestamp: The end timestamp.
        :type end_timestamp: int | None
        :param sort_by_time: Whether to sort by time.
        :type sort_by_time: bool
        :param continent: The continent to filter by.
        :type continent: str | None
        :param offset: The offset.
        :type offset: int
        :param limit: The limit.
        :type limit: int
        :param expand_updates: Whether to expand updates.
        :type expand_updates: bool
        :param max_updates: The max updates per story.
        :type max_updates: int
        :param max_articles: The max articles per update.
        :type max_articles: int
        :param reddit: Amount of reddit threads to include per update.
        :type reddit: int
        :param method: The method to use for searching.
        :type method: str
        :param obj_type: The object type to filter on.
        :type obj_type: list[str]
        :return: The stories response.
        :rtype: StoriesResponse
        """
        response = await self.client.request(
            method="GET",
            endpoint="/v1/stories",
            query={
                "query": query,
                "categories": categories,
                "start_timestamp": start_timestamp,
                "end_timestamp": end_timestamp,
                "offset": offset,
                "method": method,
                "sort_by": sort_by,
                "sort_type": sort_type,
                "continent": continent,
                "obj_type": obj_type,
                "reddit": reddit,
                "limit": limit,
                "expand_updates": expand_updates,
                "max_updates": max_updates,
                "max_articles": max_articles,
                "uuids": uuids
            },
            accept=[(StoriesResponse.__content_type__, 1.0)]
        )

        return StoriesResponse.model_validate(response.content)

    async def get_story(
        self,
        story_id: UUID | str,
        expand_updates: bool = True,
        max_updates: int = 11,
        max_articles: int = 5,
        reddit: int = 0,
    ) -> StoryResponse:
        """
        Get a single news story given the ID.

        https://docs.asknews.app/en/reference#get-/v1/stories/-story_id-

        :param story_id: The story ID or URL safe title.
        :type story_id: str
        :param expand_updates: Whether to expand updates.
        :type expand_updates: bool
        :param max_updates: The max updates per story.
        :type max_updates: int
        :param max_articles: The max articles per update.
        :type max_articles: int
        :param reddit: Amount of reddit threads to include per update.
        :type reddit: int
        :return: The story response.
        :rtype: StoryResponse
        """
        response = await self.client.request(
            method="GET",
            endpoint="/v1/stories/{story_id}",
            query={
                "expand_updates": expand_updates,
                "max_updates": max_updates,
                "max_articles": max_articles,
                "reddit": reddit
            },
            params={"story_id": story_id},
            accept=[(StoryResponse.__content_type__, 1.0)]
        )
        return StoryResponse.model_validate(response.content)
