class Log:

    @staticmethod
    def log(message, app, type = 'INFO'):
        app.logger.info(message)
        return 'LOG:' + message

    @staticmethod
    def info(message, app):
        _message = ' >> ' + message
        app.logger.info(_message)
        return _message


    @staticmethod
    def debug(message, app):
        _message = ' >> ' + message
        app.logger.debug(_message)
        return _message
    