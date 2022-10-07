from dataclasses import dataclass


@dataclass
class EmailStatus:
    """
    Domain status model
    """

    status: int = None
    email: str = None
    domain: str = None
    mx: bool = None
    disposable: bool = None
    alias: bool = None
    did_you_mean: str = None
