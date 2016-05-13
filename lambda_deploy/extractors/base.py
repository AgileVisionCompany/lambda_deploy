class BaseExtractor(object):
    """
    Base class for all lambda metadata extractors
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def get_metadata(self):
        return self._collect_metadata()

    def _collect_metadata(self):
        raise NotImplementedError("This method should be overrided")
