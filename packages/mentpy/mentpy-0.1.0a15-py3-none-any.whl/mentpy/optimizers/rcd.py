# Copyright 2023 Luis Mantilla
#
# Licensed under the Apache License, Version 2.0.
# See <http://www.apache.org/licenses/LICENSE-2.0> for details.
"""This module contains the random coordinate descent optimizer."""
from mentpy.optimizers.base import BaseOpt

import numpy as np
import random


class RCDOpt(BaseOpt):
    """Class for the random coordinate descent optimizer.

    Args
    ----
    step_size : float, optional
        The initial step size of the optimizer, by default 0.1
    adaptive : bool, optional
        Whether to use an adaptive step size, by default False

    Examples
    --------
    Create a random coordinate descent optimizer

    .. ipython:: python

        opt = mp.optimizers.RCDOpt()
        print(opt)

    Group
    -----
    optimizers
    """

    def __init__(self, step_size=0.1, adaptive=False) -> None:
        """Initialize the random coordinate descent optimizer."""
        self.step_size = step_size
        self.adaptive = adaptive

    def step(self, f, x, i, **kwargs):
        """Take a step using the random coordinate descent optimizer."""
        coord_idx = random.randint(0, len(x) - 1)
        delta = np.zeros_like(x)
        delta[coord_idx] = 1e-5
        partial_gradient = (f(x + delta) - f(x - delta)) / (2 * delta[coord_idx])

        current_step_size = self.step_size
        if self.adaptive:
            current_step_size /= np.sqrt(i + 1)

        x[coord_idx] -= current_step_size * partial_gradient

        return x

    def optimize(self, f, x0, num_iters=100, callback=None, verbose=False, **kwargs):
        """Optimize a function f using the random coordinate descent optimizer."""
        x = x0
        for i in range(num_iters):
            x = self.step(f, x, i, **kwargs)
            if callback is not None:
                callback(x, i)
            if verbose:
                print(f"Iteration {i+1}/{num_iters}")
        return x

    def update_step_size(self, x, i, factor=0.99):
        """Update the step size of the optimizer."""
        self.step_size = self.step_size * factor

    def optimize_and_gradient_norm(
        self, f, x0, num_iters=100, callback=None, verbose=False, **kwargs
    ):
        """Optimize a function f using the random coordinate descent optimizer."""
        x = x0
        coord_iters = np.zeros(len(x))
        norm = []

        for i in range(num_iters):
            # Random coordinate descent optimizer
            coord_idx = random.randint(0, len(x) - 1)
            coord_iters[coord_idx] += 1
            delta = np.zeros_like(x)
            delta[coord_idx] = 1e-5
            partial_gradient = (f(x + delta) - f(x - delta)) / (2 * delta[coord_idx])

            current_step_size = self.step_size
            if self.adaptive:
                current_step_size /= np.sqrt(coord_iters[coord_idx])

            x[coord_idx] -= current_step_size * partial_gradient

            norm.append(np.linalg.norm(partial_gradient))

            if callback is not None:
                callback(x, i)
            if verbose:
                print(f"Iteration {i+1} of {num_iters}: {x} with value {f(x)}")
        return x, norm

    def reset(self, *args, **kwargs):
        pass
