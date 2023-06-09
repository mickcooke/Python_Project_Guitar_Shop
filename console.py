import pdb
from models.guitar import Guitar
from models.maker import Maker

import repositories.guitar_repository as guitar_repository
import repositories.maker_repository as maker_repository

guitar_repository.delete_all()
