from typing import Dict, Callable
from dataclasses import dataclass, field

@dataclass
class Config:
    """Configuration config, e.g., custom operators"""

    custom_ops: Dict[str, Callable] = field(default_factory=dict)
