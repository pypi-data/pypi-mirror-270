Introduction
=============
MindTorch is MindSpore tool for adapting the PyTorch interface, which is designed to make PyTorch code perform efficiently on Ascend without changing the habits of the original PyTorch users.

|MindTorch-architecture|

Install
=======

MindTorch has some prerequisites that need to be installed first, including MindSpore, PIL, NumPy.

.. code:: bash

    # for last stable version
    pip install mindtorch

    # for latest release candidate
    pip install --upgrade --pre mindtorch

Alternatively, you can install the latest or development version by directly pulling from OpenI:

.. code:: bash

    pip3 install git+https://openi.pcl.ac.cn/OpenI/MSAdapter.git

User guide
===========
You can start using it straight away, for example:

Import mstorch_enable in the main program of the code file to adapt PyTorch code to MindTorch

.. code:: python

    from mindtorch.tools import mstorch_enable   # It needs to be used before importing torch related modules in the main program

    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    from torchvision import datasets, transforms

    class LeNet(nn.Module):
        def __init__(self):
            super(LeNet, self).__init__()
            self.conv1 = nn.Conv2d(3, 16, 5)
            self.pool1 = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(16, 32, 5)
            self.pool2 = nn.MaxPool2d(2, 2)
            self.fc1 = nn.Linear(32*5*5, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)

        def forward(self, x):
            x = F.relu(self.conv1(x))
            x = self.pool1(x)
            x = F.relu(self.conv2(x))
            x = self.pool2(x)
            x = x.view(-1, 32*5*5)
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x

    criterion = nn.CrossEntropyLoss()

    transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    train_set = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
    train_data = DataLoader(train_set, batch_size=128, shuffle=True, num_workers=2, drop_last=True)

After importing mstorch_enable, the imported module with the same name of torch will be automatically converted to the corresponding module of mindtorch when the code is executed (currently supports automatic conversion of torch, torchvision, torchaudio related modules), and then execute the .py file of the main program. For more information on how to use it, please refer to User's Guide.


License
=======

MindTorch is released under the Apache 2.0 license.

.. |MindTorch-architecture| image:: https://openi.pcl.ac.cn/OpenI/MSAdapter/raw/branch/master/doc/readthedocs/source_zh/docs/pic/MSA_F.png