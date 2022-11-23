import sqlite3

cdb = sqlite3.connect('cars.db')
k = cdb.cursor()

k.execute(
    """
        CREATE TABLE TBCars(
		        carID,
		        carbrand,
		        carmodel,
		        carprice
	        )
    """
    )

print(k.fetchall())
data = k.fetchall()
cdb.commit()
cdb.close()