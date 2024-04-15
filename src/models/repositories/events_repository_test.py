from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="New register in the database")
def test_insert_event():
    event = {
        "uuid": "my-uuid-test",
        "title": "My Title",
        "slug": "my-slug",
        "maximum_attendees": 10
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)


def test_get_event_by_id():
    event_id = "my-uuid-test1234"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
