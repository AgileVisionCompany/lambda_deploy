from .regex_extractor import RegexExtractor
from .decorator_extractor import DecoratorExtractor


def extract_metadata(
        file_name, extractors=[RegexExtractor, DecoratorExtractor]):

    metadata = None

    for extractor in extractors:
        instance = extractor(file_name=file_name)
        metadata = instance.get_metadata()

        if metadata is not None:
            return metadata

    return None
