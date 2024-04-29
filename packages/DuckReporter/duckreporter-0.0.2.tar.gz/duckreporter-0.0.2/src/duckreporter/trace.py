import logging
import time
import sys
import random
from uuid import uuid4
import os
from dataclasses import dataclass

from .emitter import Emitter


logger = logging.getLogger(__name__)

@dataclass
class FunctionCall:
    filename: str
    lineno: int
    function: str
@dataclass
class TraceStat:
    location: FunctionCall
    call_time: float
    caller: FunctionCall

class TraceDuck(object):

    def __init__(self, api_host: str, dsn: str = None):
        self._emitter = Emitter(api_host, dsn)
        self._cwd = os.getcwd()
        self._trace_in_progress = 0

    def trace(self, *args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            # Decorator is used as @trace
            return self.trace_decorator(args[0])
        else:
            # Decorator is used as @trace(...)
            return lambda func: self.trace_decorator(func, *args, **kwargs)

    def trace_decorator(self, func, *args, **kwargs):
        sample_rate = kwargs.get("sample_rate", 1.0)

        def wrapper(*func_args, **func_kwargs):
            if random.random() > sample_rate:
                return func(*func_args, **func_kwargs)
            
            if self._trace_in_progress:
                return func(*func_args, **func_kwargs)
            else:
                self._trace_in_progress = 1
        
            call_stack: list[TraceStat] = []
            trace_id = str(uuid4())

            def trace_func(frame, event, arg):
                # ignore any trace wrappers 
                if 'trace.py' in frame.f_code.co_filename and 'wrapper' in frame.f_code.co_name:
                    return
                
                nonlocal call_stack

                if event == 'call':
                    call_time = time.time()
                    current_location = FunctionCall(frame.f_code.co_filename, frame.f_code.co_firstlineno, frame.f_code.co_name)

                    caller_location = FunctionCall(frame.f_back.f_code.co_filename, frame.f_back.f_lineno, frame.f_back.f_code.co_name)
                    
                    # tracing is in progress and calls are in stack already, ignore any trace wrappers 
                    if self._trace_in_progress and call_stack and 'trace.py' in caller_location.filename and 'wrapper' in caller_location.function:
                        caller_location = FunctionCall(frame.f_back.f_back.f_code.co_filename, frame.f_back.f_back.f_lineno, frame.f_back.f_back.f_code.co_name)

                    call_stack.append(TraceStat(current_location, call_time, caller_location))

                if event == 'return':
                    trace_stat = call_stack.pop()
                    elapsed_time = time.time() - trace_stat.call_time
                    called_by = trace_stat.caller

                    formatted_stats = self.format_stats(trace_id, trace_stat.location, elapsed_time, called_by)
                    self._emitter.emit(formatted_stats)
                return trace_func
            
            sys.settrace(trace_func)
            try:
                res = func(*func_args, **func_kwargs)
            finally:
                self._trace_in_progress = 0
                sys.settrace(None)  # Disable the trace function


            return res

        return wrapper

    def format_stats(self, trace_id: str, location: FunctionCall, elapsed_time: float, caller: FunctionCall):
        # format stats to json
        return {
            "trace": [
                {
                    "uuid": str(uuid4()),
                    "trace_id": trace_id,
                    "tottime": elapsed_time,
                    "filename": location.filename,
                    "lineno": location.lineno,
                    "function": location.function,
                    "caller_filename": caller.filename,
                    "caller_lineno": caller.lineno,
                    "caller_function": caller.function,
                    "rootdir": self._cwd,
                    "relative_filename": location.filename.replace(self._cwd + "/", ""),
                    "caller_relative_filename": caller.filename.replace(self._cwd + "/", "")
                }
            ]
        }

    def close(self):
        self._emitter.flush()
