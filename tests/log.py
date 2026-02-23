import LogAssist.log as Logger

Logger.logger_init()
Logger.debug('debug', 'test message')
Logger.info('info', 'test message')
Logger.warning('warning', 'test message')
Logger.error('error', 'test message')
Logger.exception('exception', 'test message')
try:
    Logger.critical('critical', 'test message')
except Exception as e:
    print(e)
