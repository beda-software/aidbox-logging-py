# aidbox-logging-py
Aidbox $loggy python logging handler

## Installation

Install from pypi as `aidbox-logging`

## Usage

```python
from aidbox_logging import init_queued_aidbox_loggy_handler, enable_excepthook_logging


logging.basicConfig(
    format="[%(asctime)s] [%(process)d] [%(levelname)s] %(name)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %z",
)
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
if env_config.loggy_url:
    loggy_handler = init_queued_aidbox_loggy_handler(
        env_config.loggy_url,
        app="lab-backend",
        version=f"{version.__version__}-{version.__build_commit_hash__}",
        meta={
            "env": env_config.lab_room_id,
        },
    )

    # By default all log messages will be handled by loggy
    root_logger.addHandler(loggy_handler)

    # By default gunicorn errors are not propagated, so we handle it explicitly
    logging.getLogger("gunicorn.error").addHandler(loggy_handler)

    # Optional: enable excepthook logging that intercepts all exceptions inside threads
    enable_excepthook_logging()
```
