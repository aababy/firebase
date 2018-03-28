import time
import logging

def cron_print_time(signum):
    ISOTIMEFORMAT='%Y-%m-%d %X'
    print time.strftime(ISOTIMEFORMAT, time.localtime())

def cron_print_hello(signum):
    mylog = logging.getLogger('django')
    mylog.debug('@@hello')
    print "hello"

jobs = [ { "name" : cron_print_time,
           "time": [0, 17, -1, -1, 1], #minute, hour, day, month, weekday, "-1" means "all"，此例为每个周一的17：00
          },     
         { "name" : cron_print_hello,
           "time": [5],  #每隔2秒
          },    
]