"""Qui decrivo la classe che gestisce le classi delle risorse."""

# Standard Import
import dataclasses as dc

# Site-package Import

# Project Import
from dig import digger_manager as dm
from index import indexer_manager as im
from meta import metadata_manager as mm
from util import config_manager as cm
from util import logger_manager as lm
from util import option_manager as om
from util import path_manager as pm


@dc.dataclass
class ResourceManager():
    """Collezione delle risorse utili all'applicazione"""
    
    path: pm.PathManager
    
    config: cm.ConfigManager
    logger: lm.LoggerManager
    option: om.OptionManager

    indexer: im.IndexerManager
    digger: dm.DiggerManager
    metadata: mm.MetadataManager
    
    