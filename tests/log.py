import LogAssist.log as Logger

Logger.logger_init()
Logger.debug('test', 'test message')
Logger.info('test', 'test message')
Logger.warning('test', 'test message')
Logger.error('test', 'test message')
try:
    Logger.critical('test', 'test message')
except Exception as e:
    print(e)
