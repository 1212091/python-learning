class RemoveViolateRuleError(Exception):
    def __init__(self, message):
        super(RemoveViolateRuleError, self).__init__(message)