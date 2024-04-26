"""Provides a client for the Halo Infinite API."""

from functools import cached_property

from .services import (
    DiscoveryUgcService,
    GameCmsHacsService,
    ProfileService,
    SkillService,
    StatsService,
)
from .session import Session

__all__ = ["HaloInfiniteClient"]


class HaloInfiniteClient:
    """A client for the Halo Infinite API."""

    def __init__(
        self,
        session: Session,
        spartan_token: str,
        clearance_token: str,
        requests_per_second: int | None = 5,
    ) -> None:
        """Initialize a client for the Halo Infinite API.

        Args:
            session: The `aiohttp.ClientSession` to use. Support for caching is
                available via a `CachedSession` from `aiohttp-client-cache`.
            spartan_token: The spartan token used to authenticate with the API.
            clearance_token: The clearance token used to authenticate with the
                API.
            requests_per_second: The rate limit to use. Note that this rate
                limit is enforced per service, not globally. Defaults to 5
                requests per second. Set to None to disable rate limiting.
        """
        session.headers.clear()
        session.headers["Accept"] = "application/json"
        session.headers["x-343-authorization-spartan"] = spartan_token
        session.headers["343-clearance"] = clearance_token
        self._session = session
        self._requests_per_second = requests_per_second

    @cached_property
    def profile(self) -> ProfileService:
        """Profile data service. Get user data, such as XUIDs/gamertags."""
        return ProfileService(self._session, self._requests_per_second)

    @cached_property
    def gamecms_hacs(self) -> GameCmsHacsService:
        """Game content management data service (e.g., medal metadata)"""
        return GameCmsHacsService(self._session, self._requests_per_second)

    @cached_property
    def skill(self) -> SkillService:
        """Skill data service. Retrieve MMR and CSR data by match or playlist."""
        return SkillService(self._session, self._requests_per_second)

    @cached_property
    def stats(self) -> StatsService:
        """Stats data service. Retrieve match history and match stats."""
        return StatsService(self._session, self._requests_per_second)

    @cached_property
    def discovery_ugc(self) -> DiscoveryUgcService:
        """User-generated content discovery data service (maps, modes, etc.)."""
        return DiscoveryUgcService(self._session, self._requests_per_second)
