#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Debug utilities
This code was adapted from spyderlib original developed by Pierre Raybaut
spyderlib site:
http://code.google.com/p/spyderlib
"""

import StringIO
import traceback
import time


def log_time(fd):
    timestr = "Logging time: %s" % time.ctime(time.time())
    print >>fd, "="*len(timestr)
    print >>fd, timestr
    print >>fd, "="*len(timestr)
    print >>fd, ""

def log_last_error(fname, context=None):
    """Log last error in filename *fname* -- *context*: string (optional)"""
    out = StringIO.StringIO()
    traceback.print_exc(file=out)
    fd = open(fname, 'a')
    log_time(fd)
    if context:
        print >>fd, "Context"
        print >>fd, "-------"
        print >>fd, ""
        print >>fd, context
        print >>fd, ""
        print >>fd, "Traceback"
        print >>fd, "---------"
        print >>fd, ""
    traceback.print_exc(file=fd)
    print >>fd, ""
    print >>fd, ""

def log_dt(fname, context, t0):
    fd = open(fname, 'a')
    log_time(fd)
    print >>fd, "%s: %d ms" % (context, 10*round(1e2*(time.time()-t0)))
    print >>fd, ""
    print >>fd, ""
