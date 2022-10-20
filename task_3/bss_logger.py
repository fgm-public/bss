#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import syslog
from random import randrange
from time import sleep

while True:
    syslog.openlog(logoption=syslog.LOG_PID)
    interval = randrange(900)
    syslog.syslog(f'bss is the best company ever! And I need to sleep just {interval} seconds')
    syslog.closelog()
    sleep(interval)