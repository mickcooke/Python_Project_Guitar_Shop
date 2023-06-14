import pdb
from models.guitar import Guitar
from models.maker import Maker

import repositories.guitar_repository as guitar_repository
import repositories.maker_repository as maker_repository

guitar_repository.delete_all()
maker_repository.delete_all()

# CREATE AND ADD MAKERS
maker1 = Maker("Gibson", "Chad Hogan", "+01-800-444-2766", "chad@gibson.com", "true" )
maker_repository.save(maker1)
maker2 = Maker("Fender", "Maggie Simpson", "0333-200-8765", "mags@fender.com", "true" )
maker_repository.save(maker2)
maker3= Maker("Hofner", "Paul Hollywood", "01382-234785", "paul_block@hofner.co.uk", "true")
maker_repository.save(maker3)
maker4= Maker("Taylor", "Mary Berry", "0800-888-2548", "cakemaker@hotmail.com", "false")
maker_repository.save(maker4)

# CREATE AND ADD GUITARS
guitar1 = Guitar("Gibson Les Paul Standard", "50s Heritage Cherry Sunburst", 11, 10, 1500.00, 2199.00, maker1)
guitar_repository.save(guitar1)
guitar2 = Guitar("Fender Player Jazzmaster", "Shell Pink", 12, 9, 499.00, 799.00, maker2)
guitar_repository.save(guitar2)
guitar3 = Guitar("Gibson Flying V", "1967 Mahogany Reissue with Maestro Vibrola Gloss Sparkling Burgundy", 5, 6, 3999.00, 5299.00, maker1)
guitar_repository.save(guitar3)
guitar4 = Guitar("Taylor 214ce", "Grand Auditorium", 4, 3, 789.00, 999.00, maker4)
guitar_repository.save(guitar4)
guitar5 = Guitar("Fender Stratocaster", "Sunburst Maple Fingerboard", 4, 5, 450.00, 670.00, maker2)
guitar_repository.save(guitar5)
guitar6 = Guitar("Fender Telecaster", "Butterscotch Blonde Roasted Maple Neck/Fingerboard with Custom Shop Pickups", 4, 3, 740.00, 899.00, maker2)
guitar_repository.save(guitar6)


# TESTING THAT DATABASE IS POPULATING
# makers = maker_repository.select_all()
# guitars = guitar_repository.select_all()


# pdb.set_trace()

