from typing import Dict, Any, List, Optional
from .internal import meets_crit
from .config import Config

def all_meet_criteria(
    records: List[Dict[str, Any]],
    criteria: Dict[str, Any],
    config: Optional[Config] = None
) -> bool:
    """
    Determine if all of the records meet the given criteria.

    Parameters:
    - records (List[Dict[str, Any]]): The data records.
    - criteria (Dict[str, Any]): The criteria.
      Should be a dictionary representing the conditions
      that the record must satisfy. May include nested conditions.
    - config (Optional[Config]): Configuration options.
    
    Returns:
    - bool: Whether all of the records meet the criteria.
    """
    return all(meets_crit(record, criteria, config) for record in records)
