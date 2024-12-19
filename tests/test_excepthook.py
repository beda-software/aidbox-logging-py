import asyncio
import threading

from pytest_mock import MockerFixture


async def test_excepthook_catches_exceptions_in_task(mocker: MockerFixture) -> None:
    mock_logging = mocker.patch("aidbox_logging.logging.critical")

    from aidbox_logging import enable_excepthook_logging

    enable_excepthook_logging()

    async def exceptor() -> None:
        raise Exception("Inside task")

    asyncio.create_task(exceptor())

    await asyncio.sleep(0)

    mock_logging.assert_called_once()


def test_excepthook_catches_exceptions_in_thread(mocker: MockerFixture) -> None:
    mock_logging = mocker.patch("aidbox_logging.logging.critical")

    from aidbox_logging import enable_excepthook_logging

    enable_excepthook_logging()

    def exceptor() -> None:
        raise Exception("Inside thread")

    thread = threading.Thread(target=exceptor)
    thread.start()

    thread.join()

    mock_logging.assert_called_once()
