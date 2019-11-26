from flask import Blueprint, Response
from flask_restplus import Api, Resource, reqparse
from server import service

blueprint = Blueprint('base_redis_example', __name__)
api = Api(blueprint, doc="/docs")

@api.route("/example")
class Placeholder(Resource):
    
    req_schema = reqparse.RequestParser()
    req_schema.add_argument("key", type=str, required=True)
    
    add_schema = req_schema.copy()
    add_schema.add_argument("value", type=str, required=True)
    
    @api.expect(add_schema)
    def post(self):
        """ placeholder
        """
        req = self.add_schema.parse_args()
        if service.cache.exists(req.key): return Response(status=409)
        return service.cache.set(req.key, req.value)

    @api.expect(req_schema)
    def get(self):
        """ placeholder
        """
        req = self.req_schema.parse_args()
        if not service.cache.exists(req.key): return Response(status=204)
        return service.cache.get(req.key)
    
    @api.expect(add_schema)
    def put(self):
        """ placeholder
        """
        req = self.add_schema.parse_args()
        if not service.cache.exists(req.key): return Response(status=204)
        return service.cache.set(req.key, req.value)
    
    @api.expect(req_schema)
    def delete(self):
        """ placeholder
        """
        req = self.req_schema.parse_args()
        if not service.cache.exists(req.key): return Response(status=204)
        return service.cache.delete(req.key)
