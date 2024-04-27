# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mm1_torch']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'torch', 'zetascale']

setup_kwargs = {
    'name': 'mm1-torch',
    'version': '0.0.6',
    'description': 'MM1 - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# MM1 \nPyTorch Implementation of the paper "MM1: Methods, Analysis & Insights from Multimodal LLM Pre-training".\n\n`img -> encoder -> connector -> llm -> tokens`\xa0\n\n## install\n`pip3 install mm1-torch`\n\n## usage\n```python\nimport torch\nfrom mm1_torch.main import MM1\n\n# Tensors\nx = torch.randint(0, 100, (1, 512))  # Create a random tensor of shape (1, 512)\nimg = torch.randn(1, 3, 224, 224)  # Create a random image tensor of shape (1, 3, 224, 224)\n\n# Create a model\nmodel = MM1(\n    dim=512,  # Dimension of the input tensor\n    depth=12,  # Number of transformer layers\n    heads=8,  # Number of attention heads\n    dim_head=64,  # Dimension of each attention head\n    dropout=0.1,  # Dropout rate\n    num_experts=4,  # Number of experts in mixture-of-experts\n    num_experts_per_tok=2,  # Number of experts per token in mixture-of-experts\n    encoder_dim=512,  # Dimension of the encoder output\n    encoder_depth=12,  # Number of encoder transformer layers\n    encoder_heads=8,  # Number of encoder attention heads\n    use_moe=True,  # Whether to use mixture-of-experts\n    return_logits=True  # Whether to return logits or probabilities\n)\n\n# Forward\nout = model(x, img)  # Forward pass through the model\nprint(out.shape)  # Print the shape of the output tensor (torch.Size([2, 3, 512]))\nprint(out)  # Print the output tensor\n```\n\n### `CAbstractor`\n\n```python\nimport torch\nfrom mm1_torch.main import CAbstractor\n\n# Tensors\nx = torch.randn(1, 100, 512)\n\n# Create a model\nmodel = CAbstractor(\n    dim=512,\n    depth=12,\n    heads=8,\n)\n\n\n# Forward\nout = model(x)\nprint(out.shape)\n\n```\n\n\n# License\nMIT\n\n\n## Todo\n\n- [x] Implement the deformable attention\n- [ ] Create a training script for Huggingface datasets\n- [ ] Create unit tests for every module',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/mm1',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
