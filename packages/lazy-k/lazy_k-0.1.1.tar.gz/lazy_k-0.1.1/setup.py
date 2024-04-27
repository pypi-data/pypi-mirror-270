# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'lazy-k',
    'version': '0.1.1',
    'description': 'A C++ implementation of the Lazy-k algorithm (A* with partial expansion)',
    'long_description': '![main](https://github.com/ahemmershift/lazyk/actions/workflows/python.yml/badge.svg)\n# lazyk\nA C++/Python library for efficiently iterating over high-probability label-assignments.\n\n## Installation\nThe library can be installed by cloning it and installing the Python package using pip.\n\n```bash\ngit clone git@github.com:ArthurDevNL/lazyk.git\ncd lazyk\npip install -e .\n```\n\n## Usage\nThe library can be used to iterate over the high-probability label-assignments of a given probability matrix. The following example shows how to use the library to iterate over the high-probability label-assignments of a 3x3 grid.\n\n```python\nfrom lazyk import lazyk\nimport numpy as np\n\nprobs = np.arange(1, 10).reshape(3, -1)\nprobs = probs / probs.sum(axis=1, keepdims=True)\n\nfor seq in lazyk(probs, cache_assignments=True): # cache_assignments is true by default, but can be turned off\n    print(seq)\n```\n\nThe `cache_assignments` parameter indicates whether the algorithm should cache the intermediate label-assignments. This will improve the running speed of the algorithm but also require more memory. The default value is `True` but can be turned off if memory is a concern.\n',
    'author': 'Arthur Hemmer',
    'author_email': 'arthurhemmer@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/arthurdevnl/lazyk',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
