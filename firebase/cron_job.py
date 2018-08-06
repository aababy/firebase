# coding:utf-8
import time
import logging


def cron_print_time(signum):
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    log = time.strftime(ISOTIMEFORMAT, time.localtime())
    mylog = logging.getLogger('django')
    mylog.debug(log)


def cron_print_hello(signum):
    print "hello"


jobs = [{"name": cron_print_time,
         # minute, hour, day, month, weekday, "-1" means "all"，此例为每个周一的17：00
         "time": [0, 2, -1, -1, -1],
         },
        # {"name": cron_print_hello,
        #  "time": [5],  # 每隔2秒
        #  },
        ]
