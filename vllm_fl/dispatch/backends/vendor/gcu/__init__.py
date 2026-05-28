# Copyright (c) 2026 BAAI. All rights reserved.

"""
GCU (Enflame) backend for vllm-plugin-FL dispatch.
"""

from .gcu import GCUBackend


__all__ = ["GCUBackend"]
