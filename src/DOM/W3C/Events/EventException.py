#!/usr/bin/env python
from __future__ import with_statement

import PyV8

# Introduced in DOM Level 2
class EventException(RuntimeError, PyV8.JSClass):
    def __init__(self, code):
        self.code = code

    # Exception Code
    UNSPECIFIED_EVENT_TYPE_ERR      = 0 # If the Event's type was not specified by initializing the event before the
                                        # method was called. Specification of the Event's type as null or an empty
                                        #string will also trigger this exception.

