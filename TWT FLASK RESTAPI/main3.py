from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

videos_put_args = reqparse.RequestParser()
videos_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
videos_put_args.add_argument("likes", type=int, help="likes of the video is required", required=True)
videos_put_args.add_argument("views", type=int, help="views of the video is required", required=True)

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id):
        args = videos_put_args.parse_args()
        return {video_id: args}
    
api.add_resource(Video, '/video/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)