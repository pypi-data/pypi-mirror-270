# Copyright 2023 Luis Mantilla
#
# Licensed under the Apache License, Version 2.0.
# See <http://www.apache.org/licenses/LICENSE-2.0> for details.
"""Module to calculate gradients using the finite difference method."""
import numpy as np


def fd_gradient(f, x, h=1e-5, type="central"):
    if type not in ["central", "forward", "backward"]:
        raise UserWarning(
            f"Expected type to be 'central', 'forward', or 'backward' but {type} was given"
        )

    grad = np.zeros(len(x))
    for i in range(len(x)):
        if type == "central":
            grad[i] = (f(x + h * np.eye(len(x))[i]) - f(x - h * np.eye(len(x))[i])) / (
                2 * h
            )
        elif type == "forward":
            grad[i] = (f(x + h * np.eye(len(x))[i]) - f(x)) / h
        elif type == "backward":
            grad[i] = (f(x) - f(x - h * np.eye(len(x))[i])) / h
    return grad


def fd_hessian(f, x, h=1e-5, type="central"):
    if type not in ["central", "forward", "backward"]:
        raise UserWarning(
            f"Expected type to be 'central', 'forward', or 'backward' but {type} was given"
        )

    hess = np.zeros((len(x), len(x)))
    for i in range(len(x)):
        for j in range(len(x)):
            if type == "central":
                hess[i, j] = (
                    f(x + h * np.eye(len(x))[i] + h * np.eye(len(x))[j])
                    - f(x + h * np.eye(len(x))[i] - h * np.eye(len(x))[j])
                    - f(x - h * np.eye(len(x))[i] + h * np.eye(len(x))[j])
                    + f(x - h * np.eye(len(x))[i] - h * np.eye(len(x))[j])
                ) / (4 * h**2)
            elif type == "forward":
                hess[i, j] = (
                    f(x + h * np.eye(len(x))[i] + h * np.eye(len(x))[j])
                    - f(x + h * np.eye(len(x))[i])
                    - f(x + h * np.eye(len(x))[j])
                    + f(x)
                ) / h**2
            elif type == "backward":
                hess[i, j] = (
                    f(x)
                    - f(x - h * np.eye(len(x))[i])
                    - f(x - h * np.eye(len(x))[j])
                    + f(x - h * np.eye(len(x))[i] - h * np.eye(len(x))[j])
                ) / h**2
    return hess
