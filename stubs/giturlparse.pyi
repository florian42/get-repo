# Function bodies cannot be completely removed. By convention,
# we replace them with `...` instead of the `pass` statement.
from typing import Optional

class Url:
    resource: Optional[str]
    owner: Optional[str]
    name: Optional[str]

def parse(url: str) -> Url: ...
