import re

from .base import BaseExtractor


class RegexExtractor(BaseExtractor):

    def __init__(self, *args, **kwargs):

        if getattr(self, 'function_name_pattern', None) is None:
            self.function_name_pattern = kwargs.get(
                'function_name_pattern', '.*@@LambdaFunction\.name[\s]*=[\s]*([a-zA-Z0-9-_]+)')

        super(RegexExtractor, self).__init__(*args, **kwargs)

    def _collect_metadata(self):
        function_name_regex = re.compile(self.function_name_pattern)
        metadata = dict()
        with open(self.file_name, 'r') as fp:
            for line in fp:
                stripped_line = line.strip()
                matches = function_name_regex.match(stripped_line)
                if matches is not None:
                    metadata['function_name'] = matches.group(1)
                    return metadata

        return None
