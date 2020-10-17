Pip-installable fork of https://github.com/kylebgorman/syllabify.

Installation:
```
git clone https://github.com/kylebgorman/syllabify.git
pip install -e syllabify
```

Usage:
```
from syllabify import syllabify, wcm

syllabify('AH0 L AE1 S K AH0'.split())
# Out: [([], ['AH0'], []), (['L'], ['AE1'], ['S']), (['K'], ['AH0'], [])]
```

=== Port for Python3

syllabify.py is a Python module for syllabifying ARPABET transcriptions; 
the method used is informed by subtle details of English phonology.

* See `manual.pdf` for usage
* See `syllabify.py` for the license and API
