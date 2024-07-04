#!/usr/bin/env python3
from typing import Sequence, List, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Python annotations
    """
    return [(i, len(i)) for i in lst]
