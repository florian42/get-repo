from typing import Optional

class Url:
    resource: Optional[str]
    owner: Optional[str]
    name: Optional[str]

def parse(url: str) -> Url: ...
