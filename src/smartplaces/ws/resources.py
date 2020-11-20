from __future__ import absolute_import, annotations

from flask import request
from flask_restful import Resource

from smartplaces.common.models.place import Place


class ResourcesBuilder:

    @staticmethod
    def routes():
        return [(PlaceResource, '/place', ())]


class PlaceResource(Resource):
    """
    The Resource for the management of the places of interest
    """

    PLACE_ID_KEY = "place_id"

    def get(self):
        place_id: str = request.args.get(self.PLACE_ID_KEY)
        if not place_id:
            return {"message": "Malformed request: missing required `place_id` parameter"}, 400

        # return the place with the place_id equal to the requested one

    def post(self):
        posted_data = request.get_json()
        if posted_data is None:
            return {"message": "Data is missing"}, 400

        try:
            place: Place = Place.from_repr(posted_data)
        except KeyError:
            return {"message": "Could not parse posted data: malformed request"}, 400

        # save the place

    def put(self):
        posted_data = request.get_json()
        if posted_data is None:
            return {"message": "Data is missing"}, 400

        try:
            place: Place = Place.from_repr(posted_data)
        except KeyError:
            return {"message": "Could not parse posted data: malformed request"}, 400

        # does it make sense to update a place?

    def delete(self):
        place_id: str = request.args.get(self.PLACE_ID_KEY)
        if not place_id:
            return {"message": "Malformed request: missing required `place_id` parameter"}, 400

        # delete the place
