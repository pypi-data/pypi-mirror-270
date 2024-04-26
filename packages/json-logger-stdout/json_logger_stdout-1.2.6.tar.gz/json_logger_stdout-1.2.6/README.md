# JSON Logger Stdout
##### Log to the stdout directly so that they can be consumed by some centralized log collecting service like Fluentd.
=================================================================================================

JSON Logger for MicroServices. Prints logs to the stdout of the service and can be shipped to ES by leveraging a centralized tool like Fluentd
> Usage Examples
`json_std_logger` is the log object that the library exports and it exposes methods for all log levels which is shown in the examples. This is an instance of the class `JSONLoggerStdout`

> Important Note: By default the log level is set at `INFO`. Please change it using the `setLevel` method which is exposed out.


```bash
from json_logger_stdout import JSONStdFormatter, json_std_logger

#By Default the log level is INFO

json_std_logger.error('error log')      # {"timestamp": "2022-01-21T06:36:32.668292Z", "level": "ERROR", "message": "error log"}
json_std_logger.info('info log')        # {"timestamp": "2022-01-21T06:36:32.668420Z", "level": "INFO", "message": "info log"}
json_std_logger.debug('debug log, no print')      # Prints Nothing as the current level by default is INFO

import logging
json_std_logger.setLevel(logging.DEBUG) # Set Log Level
json_std_logger.debug('debug log')      # {"timestamp": "2022-01-21T06:36:32.668476Z", "level": "DEBUG", "message": "debug log"}

```

### List of Exposed Methods
`getLogger` : Returns the already initialized log object.

`setLevel` : Sets Log Level. Pass any valid log level from the python `logging` module.

`setFormatter` : Sets a custom log formatter if needed. This call will clear out all the other handlers, so please call this before adding more log handlers. It takes two arguments, the first one is simply a string that takes the fields to print in the final log. See `#Example-Set-Formatter-1` for more details.
It is possible to use a different log formatter altogether and use the second parameter to pass the log formatter object. See `#Example-Set-Formatter-2` for more details.

`addHandlers` : Pass an array of log handlers that will be attached to the log object.

### Extra Params for the logger instance
You can also configure permanent extra params to be used for a log object if you prefer not to mention it everytime in your log messages. You can either pass the params in during initializing a new `JSONLoggerStdout` instance or adding them using the `_setParams` method in the `json_std_logger`.
```bash
from json_logger_stdout import JSONLoggerStdout
logger = JSONLoggerStdout(
    service="Running Service",
    id="CAT-232"
)
logger.error('error log')          # {"timestamp": "2023-03-17T16:11:32.858440Z", "level": "ERROR", "message": "error log", "service": "Running Service", "id": "CAT-232"}
```
```bash
from json_logger_stdout import json_std_logger
json_std_logger._setParams(
    service="Different Service",
    id="ASD-233"
)
json_std_logger.info('info log')            # {"timestamp": "2023-03-17T16:11:32.858540Z", "level": "INFO", "message": "info log", "service": "Different Service", "id": "ASD-233"}
```

### Advanced Usage
The package exposes two classes `JSONLoggerStdout` & `JSONStdFormatter`
It is possible for the user to get a different log object by using the base class `JSONLoggerStdout`
```
json_logger = JSONLoggerStdout(loggerName=<optional>)
```

> NOTE : All the unnamed parameters that are passed to the logger would be converted to string and concatenated with a space ` `.
However sending named parameters to the logger would add the keys as extra parameters in the log record. Please see the last example for more clarity on this.
```bash
json_std_logger.setFormatter('%(timestamp)s %(level)s %(name) %(filename)s %(lineno)s %(module)s %(message)s')     # Example-Set-Formatter-1
json_std_logger.setFormatter(None, JSONStdFormatter('%(timestamp)s %(level)s %(name) %(filename)s %(lineno)s %(message)s'))   # Example-Set-Formatter-2

# Usage with variable parameters and named parameters to the logger.
json_std_logger.debug({'unnamedObjKey1': 'will print in message'}, {'unnamedObjKey2': 'should be concatenated with the previous part'}, extra='Named Parameter, so will be addded as an extra parameter')
# {"timestamp": "2022-01-21T07:40:03.363500Z", "level": "DEBUG", "name": "root", "filename": "json_logger_stdout.py", "lineno": 67, "module": "json_logger_stdout", "message": "{'unnamedObjKey1': 'will print in message'}, {'unnamedObjKey2': 'should be concatenated with the previous part'}", "extra": "Named Parameter, so will be addded as an extra parameter"}
```
