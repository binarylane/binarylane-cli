from __future__ import annotations

from types import MethodType
from typing import Any, Generic, List, Tuple, Type, TypedDict, TypeVar, Union

from binarylane.console.config import Config
from binarylane.console.runners import Runner
from binarylane.console.runners.command import CommandRunner

T = TypeVar("T", bound=CommandRunner)


class MockResponse(TypedDict):
    status_code: int
    received: Any


class TypeRunner(Runner, Generic[T]):
    """TypeRunner is used as parent (root) runner for runner being tested.

    The constructor accepts type (class) of Runner, whic is instantiated and
    available via the `test` property.

    Most runners do not function correctly as a root runner, so should be
    "wrapped" in TypeRunner to match normal runtime conditions.
    """

    _test: T

    _mock_response: Union[MockResponse, None]

    def __init__(self, runner_type: Type[T]) -> None:
        super().__init__(None)
        self._test = runner_type(self)

        # allow for mock responses
        self._mock_response = None
        old_request = self._test.request
        harness = self

        def sample_method(self: CommandRunner, client: Any, request: Any) -> Tuple[int, Any]:
            if harness._mock_response:
                return harness._mock_response["status_code"], harness._mock_response["received"]
            else:
                return old_request(client, request)

        self._test.request = MethodType(sample_method, self._test)  # type: ignore

    @property
    def test(self) -> T:
        return self._test

    @property
    def name(self) -> str:
        return "test"

    @property
    def description(self) -> str:
        return "test"

    def setMockResponse(self, status_code: int, received: Any) -> None:
        self._mock_response = MockResponse(status_code=status_code, received=received)

    def clearMockResponse(self) -> None:
        self._mock_response = None

    def run(self, args: List[str]) -> None:
        assert self._test is not None

        # Use a stock config
        config = getattr(self._test, "_config", None)
        if isinstance(config, Config):
            config.api_token = "example_token"

        self._test.run(args)
