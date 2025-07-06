# modules/__init__.py
"""
Módulos principais do JetBrains Trial Reset

Exporta os principais componentes para acesso direto via:
from modules import banner, admin_check, etc
"""

from . import (
    admin_check,
    banner,
    constants,
    file_cleaner,
    logging,
    menu,
    process_utils,
    registry_cleaner
)

__all__ = [
    'admin_check',
    'banner',
    'constants',
    'file_cleaner',
    'logging',
    'menu',
    'process_utils',
    'registry_cleaner'
]