# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mh_moe']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'swarms', 'torch', 'zetascale']

setup_kwargs = {
    'name': 'mh-moe',
    'version': '0.0.2',
    'description': 'Paper - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Multi-Head Mixture of Experts (MHMoE)\n\nMH-MoE to collectively attend to information from various representation\nspaces within different experts to deepen context understanding while significantly enhancing expert activation. \n\n## install\n`pip3 install mh-moe`\n\n\n## usage\n```python\nimport torch\nfrom mh_moe.main import MHMoE\n\n# Define model parameters\ndim = 512\nheads = 8\nnum_experts = 4\nnum_layers = 3\n\n# Create MHMoE model instance\nmodel = MHMoE(dim, heads, num_experts, num_layers)\n\n# Generate dummy input\nbatch_size = 10\nseq_length = 20\ndummy_input = torch.rand(batch_size, seq_length, dim)\ndummy_mask = torch.ones(batch_size, seq_length)  # Example mask\n\n# Forward pass through the model\noutput = model(dummy_input, dummy_mask)\n\n# Print output and its shape\nprint(output)\nprint(output.shape)\n```',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/MHMoE',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
