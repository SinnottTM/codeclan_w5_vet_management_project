# from database.run_sql import run_sql

# from models.booking import Booking
# from models.vet import Vet
# from models.kaiju import Kaiju
# import repositories.kaiju_repository as kaiju_repository
# import repositories.vet_repository as vet_repository

# def save(booking):
#     sql = "INSERT INTO bookings (monday, tuesday, wednesday, thursday, friday, morning, afternoon, vet_id) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s ) RETURNING *"
#     values = [booking.monday, booking.tuesday, booking.wednesday, booking.thursday, booking.friday, booking.morning, booking.afternoon, booking.vet.id]
#     results = run_sql( sql, values )
#     booking.id = results[0]['id']
#     # return booking

# def select_all():
#     bookings = []
#     sql = "SELECT * FROM bookings"
#     results = run_sql(sql)
#     for row in results:
#         booking = Booking(row['monday'], row['tuesday'], row['wednesday'], row['thursday'], row['friday'], row['morning'], row['afternoon'], row['vet_id'])
#         bookings.append(booking)
#     return bookings

# def update(booking):
#     sql = "UPDATE bookings SET bookings (monday, tuesday, wednesday, thursday, friday, morning, afternoon, vet_id) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s ) WHERE id = %s"
#     values = [booking.monday, booking.tuesday, booking.wednesday, booking.thursday, booking.friday, booking.morning, booking.afternoon, booking.vet.id]
#     run_sql(sql, values)

# def delete_all_bookings():
#     sql = "DELETE FROM bookings"
#     run_sql(sql)

# def delete_single_booking(id):
#     sql = "DELETE FROM bookings WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)
