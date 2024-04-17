from .attendees_repository import AttendeeRepository
from src.models.settings.connection import db_connection_handler
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="New register in the database")
def test_insert_attendee(): 
    event_id = "6e31d17b-92df-4c6e-b58f-e9f88e388f57"
    attendees_info = {
        "uuid": "attendee",
        "name": "Attendee Name",
        "email": "attendee@email.com",
        "event_id": event_id
    }
    attendee_repository = AttendeeRepository()
    response = attendee_repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason="...")
def test_get_attendee_badge_by_id():
    attendee_id = "meu_uuid_attendee"
    attendee_repository = AttendeeRepository()
    response = attendee_repository.get_attendee_badge_by_id(attendee_id)
    print(response)