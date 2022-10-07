from dataclasses import dataclass


@dataclass
class DomainStatus:
    """
    Domain status model
    """

    status: int = None
    domain: str = None
    mx: bool = None
    disposable: bool = None
