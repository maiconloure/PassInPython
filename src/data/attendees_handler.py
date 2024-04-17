import uuid
from src.models.repositories.attendees_repository import AttendeesRepository
from src.models.repositories.events_repository import EventsRepository
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

class AttendeesHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
        self.__events_repository = EventsRepository()

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        event_id = http_request.param["event_id"]

        event_attendees_count = self.__events_repository.count_event_attendees(event_id)

        if (
            event_attendees_count["attendeesAmount"] >= event_attendees_count["maximumAttendees"]
        ): raise Exception("Event is full")

        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id
        self.__attendees_repository.insert_attendee(body)

        return HttpResponse(body=None, status_code=201)
    
    def find_attendee_badge(self, http_request: HttpRequest) -> HttpResponse:
        attendeeId = http_request.param["attendee_id"]
        badge = self.__attendees_repository.get_attendee_badge_by_id(attendeeId)
        if not badge: raise Exception("Badge not found")

        return HttpResponse(
            body={
                "badge": {
                    "name": badge.name,
                    "email": badge.email,
                    "eventTitle": badge.title
                },
            },
            status_code=200
        )
    

    def find_attendees_from_event(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        attendees = self.__attendees_repository.get_attendees_from_event(event_id)
        if not attendees: raise Exception("Attendees not found")

        formatted_attendees = []
        for attendee in attendees:
            formatted_attendees.append(
                {
                    "id": attendee.id,
                    "name": attendee.name,
                    "email": attendee.email,
                    "checkInAt": attendee.checkInAt,
                    "created_at": attendee.createdAt
                }
            )

        return HttpResponse(
            body={ "attendees": formatted_attendees },
            status_code=200
        )