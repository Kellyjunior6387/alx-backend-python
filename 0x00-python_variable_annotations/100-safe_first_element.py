#!/usr/bin/python3
# The types of the elements of the input are not know
from typing import Any, Sequence, Optional, Union
def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
