import logging
from typing import Callable, Optional

from .extractors.base_extractor import BaseExtractor
from .extractors.pdf_text_extractor import PDFExtractor

_extractors: dict = {}
_logger = logging.getLogger(__name__)


def register_extractor(extractor_type: str) -> Callable:
    def decorator(extractor_cls: Callable) -> Callable:
        _extractors[extractor_type] = extractor_cls
        return extractor_cls

    return decorator


@register_extractor(".pdf")
def pdf_extractor(settings: Optional[dict] = None) -> PDFExtractor:
    """
    Create and return a PDFExtractor instance.
    """
    return PDFExtractor(settings)


def get_extractor(extractor_type: str, settings: Optional[dict] = None) -> BaseExtractor:
    """
    Get an extractor instance based on the extractor_type.

    Args:
    - extractor_type (str): Type of extractor to be retrieved
    - settings: Settings specific to the extractor

    Returns:
    - BaseExtractor: Instance of the specified extractor type
    """
    _logger.info("The extractor type is: " + extractor_type)
    extractor_class = _extractors.get(extractor_type)
    if extractor_class:
        _logger.info(f"Retrieving {extractor_type} extractor instance")
        extractor_instance = extractor_class(settings)
        return extractor_instance
    else:
        _logger.error("Invalid extractor type")
        raise KeyError("Invalid extractor type")
