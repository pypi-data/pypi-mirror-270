"""This module gathers MAVT aggregators.
"""
from ..internal.core.aggregators import (
    OWA,
    ULOWA,
    ChoquetIntegral,
    NormalizedWeightedSum,
    Sum,
    WeightedSum,
)

__all__ = [
    "OWA",
    "ULOWA",
    "ChoquetIntegral",
    "NormalizedWeightedSum",
    "Sum",
    "WeightedSum",
]
