import logging

import torch
from torch import nn

logger = logging.getLogger(__name__)


class Base(nn.Module):
    @classmethod
    def from_device(cls, device, *args, dtype=torch.float64, **kwargs):
        model = cls(*args, **kwargs)

        if device.type == "cuda" and torch.cuda.device_count() > 1:
            model = nn.DataParallel(model)

        model = model.to(device)

        if dtype is not None:
            model = model.to(dtype=dtype)

        return model

    @property
    def device(self):
        return next(self.parameters()).device

    @property
    def dtype(self):
        return next(self.parameters()).dtype