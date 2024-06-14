# dlt-repro

A simple repro for a dlt-sentry issue (https://github.com/dlt-hub/dlt/issues/1446)

## How to reproduce

1. clone this repo
2. create a virtual environment (`python -m venv .venv`)
3. activate the virtual environment (`source .venv/bin/activate`)
4. install the requirements (`pip install -r requirements.txt`)
5. run the pipeline, first without a Sentry DSN, and then with one:

```bash
python pipeline.py
RUNTIME__SENTRY_DSN=<MY-DSN> python pipeline.py
```

On the second invocation, you should see the following trace:

```
2024-06-14 15:17:38,342|[WARNING              ]|19598|140616593340224|dlt|logger.py|suppress_and_warn:41|Suppressed exception
Traceback (most recent call last):
  File "/home/tco/open/dlt-repro/.venv/lib/python3.10/site-packages/dlt/common/logger.py", line 39, in suppress_and_warn
    yield
  File "/home/tco/open/dlt-repro/.venv/lib/python3.10/site-packages/dlt/pipeline/trace.py", line 246, in start_trace_step
    module.on_start_trace_step(trace, step, pipeline)
  File "/home/tco/open/dlt-repro/.venv/lib/python3.10/site-packages/dlt/pipeline/track.py", line 76, in on_start_trace_step
    span = Hub.current.scope.span.start_child(description=step, op=step).__enter__()
AttributeError: 'NoneType' object has no attribute 'start_child'
2024-06-14 15:17:38,393|[WARNING              ]|19598|140616593340224|dlt|logger.py|suppress_and_warn:41|Suppressed exception
Traceback (most recent call last):
  File "/home/tco/open/dlt-repro/.venv/lib/python3.10/site-packages/dlt/common/logger.py", line 39, in suppress_and_warn
    yield
  File "/home/tco/open/dlt-repro/.venv/lib/python3.10/site-packages/dlt/pipeline/trace.py", line 246, in start_trace_step
    module.on_start_trace_step(trace, step, pipeline)
  File "/home/tco/open/dlt-repro/.venv/lib/python3.10/site-packages/dlt/pipeline/track.py", line 76, in on_start_trace_step
    span = Hub.current.scope.span.start_child(description=step, op=step).__enter__()
AttributeError: 'NoneType' object has no attribute 'start_child'
2024-06-14 15:17:38,436|[WARNING              ]|19598|140616593340224|dlt|logger.py|suppress_and_warn:41|Suppressed exception
Traceback (most recent call last):
  File "/home/tco/open/dlt-repro/.venv/lib/python3.10/site-packages/dlt/common/logger.py", line 39, in suppress_and_warn
    yield
  File "/home/tco/open/dlt-repro/.venv/lib/python3.10/site-packages/dlt/pipeline/trace.py", line 246, in start_trace_step
    module.on_start_trace_step(trace, step, pipeline)
  File "/home/tco/open/dlt-repro/.venv/lib/python3.10/site-packages/dlt/pipeline/track.py", line 76, in on_start_trace_step
    span = Hub.current.scope.span.start_child(description=step, op=step).__enter__()
AttributeError: 'NoneType' object has no attribute 'start_child'
2024-06-14 15:17:38,784|[WARNING              ]|19598|140616593340224|dlt|logger.py|suppress_and_warn:41|Suppressed exception
Traceback (most recent call last):
  File "/home/tco/open/dlt-repro/.venv/lib/python3.10/site-packages/dlt/common/logger.py", line 39, in suppress_and_warn
    yield
  File "/home/tco/open/dlt-repro/.venv/lib/python3.10/site-packages/dlt/pipeline/trace.py", line 246, in start_trace_step
    module.on_start_trace_step(trace, step, pipeline)
  File "/home/tco/open/dlt-repro/.venv/lib/python3.10/site-packages/dlt/pipeline/track.py", line 76, in on_start_trace_step
    span = Hub.current.scope.span.start_child(description=step, op=step).__enter__()
AttributeError: 'NoneType' object has no attribute 'start_child'
Pipeline pipe load step completed in 0.20 seconds
1 load package(s) were loaded to destination duckdb and into dataset pipe_dataset
The duckdb destination used duckdb:////home/tco/open/dlt-repro/pipe.duckdb location to store data
Load package 1718399858.4084966 is LOADED and contains no failed jobs
```