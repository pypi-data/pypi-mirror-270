from typing import Dict, Any, Optional
from .compare import compare
from ..config import Config

def meets_crit(
    record: Dict[str, Any],
    element: Dict[str, Any],
    config: Optional[Config] = None
) -> bool:
    """
    Internal function to check if a record meets the given criteria.

    Parameters:
    - record (Dict[str, Any]): The data record.
    - element (Dict[str, Any]): The element of the criteria.
    - config (Optional[Config]): Configuration options.

    Returns:
    - bool: Whether or not the record meets the criteria.
    """

    if not isinstance(element, dict):
        raise ValueError('Invalid element: must be a dictionary')

    # AND, OR, NOT operators
    if 'AND' in element:
        return all(meets_crit(record, el, config) for el in element.get('AND', []))
    if 'OR' in element:
        return any(meets_crit(record, el, config) for el in element.get('OR', []))
    if 'NOT' in element:
        return not meets_crit(record, element.get('NOT', {}), config)

    # Conditions
    key = element.get('key')
    operator = element.get('op')
    value = element.get('value')

    if not isinstance(key, str) or not operator or value is None:
        raise ValueError(f'Invalid condition: {element}')

    return compare(record.get(key), operator, value, config)
