# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import nemo_run as run

from nemo.lightning.pytorch.optim import PytorchOptimizerModule


@run.cli.factory
def pytorch_adam_with_flat_lr(
    lr: float = 1e-5,
) -> run.Config[PytorchOptimizerModule]:
    from torch.optim import Adam

    return run.Config(
        PytorchOptimizerModule,
        optimizer_fn=run.Partial(
            Adam,
            lr=lr,
            weight_decay=0.1,
            betas=(0.9, 0.95),
            eps=1e-8,
        ),
    )