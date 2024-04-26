# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['screcode']

package_data = \
{'': ['*']}

install_requires = \
['adjustText>=0.7',
 'anndata>=0.8.0',
 'datetime>=4.0',
 'matplotlib>=3.4.3',
 'numpy>=1.20',
 'pandas>=2.0.0',
 'scanpy>=1.9.3',
 'scikit-learn>=0.24',
 'scipy>=1.8.1,<2.0.0',
 'seaborn>=0.11.2']

setup_kwargs = {
    'name': 'screcode',
    'version': '1.0.0',
    'description': 'RECODE - resolution of the curse of dimensionality in single-cell data analysis',
    'long_description': '# RECODE - python code\n\n### Installation\n\nTo install RECODE package, use `pip` as follows:\n\n```\n$ pip install screcode\n```\n\n### Documentation\n\n[Tutorials and API reference](https://yusuke-imoto-lab.github.io/RECODE/index.html)\n\n\n### Requirements\n* Python3\n* numpy\n* scipy\n* scikit-learn\n',
    'author': 'Yusuke Imoto',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yusuke-imoto-lab/RECODE',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.20',
}


setup(**setup_kwargs)
