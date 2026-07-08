from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class LTCRecord:
    raw: Dict[str, Any]

    def get(self, key: str, default=None):
        return self.raw.get(key, default)
