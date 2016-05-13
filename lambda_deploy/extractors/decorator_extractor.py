from .regex_extractor import RegexExtractor


class DecoratorExtractor(RegexExtractor):

        def __init__(self, *args, **kwargs):

            self.function_name_pattern = '\s*@lambda_function\s*\(\s*name\s*=\s*["\']([a-zA-Z0-9-_]+)["\']'
            super(DecoratorExtractor, self).__init__(*args, **kwargs)
