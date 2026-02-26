import torch
from torch.distributions.distribution import Distribution

# Avoid validation that calls .item() during meta initialization
Distribution.set_default_validate_args(False)