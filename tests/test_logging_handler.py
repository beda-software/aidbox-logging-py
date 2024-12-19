import logging
import time

from pytest_mock import MockerFixture


def test_logging_handler(mocker: MockerFixture) -> None:
    mock_requests_post = mocker.patch("aidbox_logging.requests.post")

    from aidbox_logging import init_queued_aidbox_loggy_handler

    handler = init_queued_aidbox_loggy_handler(
        "http://example.com/$loggy", "tests", "0.1.0", meta={"default_param": "default"}
    )
    logging.getLogger().addHandler(handler)

    logging.error("Error from test", extra={"meta": {"extra_param": "extra"}})

    time.sleep(1)

    mock_requests_post.assert_called_once_with(
        "http://example.com/$loggy",
        json={
            "type": "tests-ERROR",
            "v": "0.1.0",
            "message": {
                "message": "Error from test",
                "meta": {
                    "default_param": "default",
                    "extra_param": "extra",
                    "version": "0.1.0",
                    "app": "tests",
                    "level": "ERROR",
                    "logger": "root",
                },
            },
        },
    )
