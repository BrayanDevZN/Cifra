"""
junta o controle do banco de dados com a engine
"""

from infra.manage import enginedb
from repository.manage import ControlDb

control_db = ControlDb(engine=enginedb)