"""Qui decrivo la classe che gestisce le classi delle risorse."""

# Standard Import
import dataclasses as dc

# Site-package Import

# Project Import
from meta import metadata_manager as mm
from util import config_manager as cm
from util import logger_manager as lm
from util import option_manager as om


@dc.dataclass
class ResourceManager():
    """Collezione delle risorse utili all'applicazione"""
    
    config: cm.ConfigManager
    logger: lm.LoggerManager
    option: om.OptionManager

    metadata: mm.MetadataManager