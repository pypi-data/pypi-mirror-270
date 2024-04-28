from typing import Dict, Any, List, Optional
from .internal import meets_crit
from .config import Config

def find_using_criteria(
    records: List[Dict[str, Any]],
    criteria: Dict[str, Any],
    config: Optional[Config] = None
) -> Dict[str, Any] | None:
    """
    Find the first record that meets the given criteria. Returns `None` if none found.

    Parameters:
    - records (List[Dict[str, Any]]): The data records.
    - criteria (Dict[str, Any]): The criteria.
      Should be a dictionary representing the conditions
      that the record must satisfy. May include nested conditions.
    - config (Optional[Config]): Configuration options.
    
    Returns:
    - Dict[str, Any] | None: The first record that meets the criteria, otherwise None.
    """
    return next((record for record in records if meets_crit(record, criteria, config)), None)
