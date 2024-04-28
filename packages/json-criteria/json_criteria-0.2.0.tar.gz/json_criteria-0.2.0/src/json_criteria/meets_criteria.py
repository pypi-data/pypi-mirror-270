"""Module providing a function to determine if a record meets the given criteria."""

from typing import Dict, Any, Optional
from .internal import meets_crit
from .config import Config

def meets_criteria(
    record: Dict[str, Any],
    criteria: Dict[str, Any],
    config: Optional[Config] = None
) -> bool:
    """
    Determine if a record meets the given criteria.

    Parameters:
    - record (Dict[str, Any]): The data record.
    - criteria (Dict[str, Any]): The criteria.
      Should be a dictionary representing the conditions
      that the record must satisfy. May include nested conditions.
    - config (Optional[Config]): Configuration options.
    
    Returns:
    - bool: Whether or not the record meets the criteria.
    """
    return meets_crit(record, criteria, config)
