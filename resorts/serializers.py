from builtins import object

class ResortSerializer(object):
    def __init__(self, body):
        self.body = body

    @property
    def all_resorts(self):
        output = []

        for resort in self.body:
            resort_details = {
                'id': resort.id,
                'name': resort.name,
                'description':resort.description,
                'latitude':resort.latitude,
                'longitude':resort.longitude,
                'website':resort.website,
                'likes':resort.likes,
                'comments':[]
            }
            for comment in resort.comments.all(): #add all() here because without all(), its not query set;
                comment_details={
                    'id': comment.id,
                    'body': comment.body,
                    'likes':comment.likes,
                    'resort_id':resort.id,
                    'author': comment.author
                }
                resort_details['comments'].append(comment_details)
            output.append(resort_details)

        return output

    @property
    def resort_detail(self):
        resort_details = {
            'id': self.body.id,
            'name': self.body.name,
            'description':self.body.description,
            'latitude':self.body.latitude,
            'longitude':self.body.longitude,
            'website':self.body.website,
            'likes':self.body.likes,
            'comments':[]
        }
        for comment in self.body.comments.all():
            comment_details={
                    'id': comment.id,
                    'likes': comment.likes,
                    'body': comment.body,
                    'resort_id':comment.resort.id,
                    'author': comment.author
                }
            resort_details['comments'].append(comment_details)
        return resort_details

class CommentSerializer(object):
    def __init__(self, body):
        self.body = body

    @property
    def comment_detail(self):
        comment_details = {
            'id':self.body.id,
            'likes': self.body.likes,
            'body': self.body.body,
            'resort_id': self.body.resort.id,
            'author': self.body.author

        }
        
        return comment_details