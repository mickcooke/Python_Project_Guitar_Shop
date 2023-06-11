import pdb
from models.guitar import Guitar
from models.maker import Maker

import repositories.guitar_repository as guitar_repository
import repositories.maker_repository as maker_repository

guitar_repository.delete_all()
maker_repository.delete_all()

maker1 = Maker("Gibson", "Chad Hogan", "+01-800-444-2766", "chad@gibson.com", "true" )
maker_repository.save(maker1)
maker2 = Maker("Fender", "Maggie Simpson", "0333-200-8765", "mags@fender.com", "true" )
maker_repository.save(maker2)
maker3= Maker("Hofner", "Paul Block", "01382-234785", "paul_block@hofner.co.uk", "true")
maker_repository.save(maker3)

guitar1 = Guitar("Gibson Les Paul Standard", "50s Heritage Cherry Sunburst", 11, 10, 1500.00, 2199.00, maker1)
guitar_repository.save(guitar1)
guitar2 = Guitar("Fender Player Jazzmaster", "Shell Pink", 12, 9, 499.00, 799.00, maker2)
guitar_repository.save(guitar2)

makers = maker_repository.select_all()
guitars = guitar_repository.select_all()


pdb.set_trace()

