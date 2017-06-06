class MongoUtils(object):
    mongo = None

    def __init__(self, mongo):
        self.mongo = mongo
        self.tenders = 'tenders'

    def get_by_municipality(self):
        return \
            self.mongo.db[self.tenders].aggregate([{'$group': {"_id": {'name': "$IdOpstina"}, "y": {"$sum": 1}}},
                                                   {"$project": {"_id": 1, 'y': 1}}])['result']

    def get_procedures(self):
        return \
            self.mongo.db[self.tenders].aggregate([{'$group': {"_id": {'name': "$IdVrstaPostupka"}, "y": {"$sum": 1}}},
                                                   {"$project": {"_id": 1, 'y': 1}}])['result']

    def get_activities(self):
        return \
            self.mongo.db[self.tenders].aggregate([{'$group': {"_id": {'name': "$IdDelatnost"}, "y": {"$sum": 1}}},
                                                   {"$project": {"_id": 1, 'y': 1}}, {'$sort': {'y': -1}},
                                                   {'$limit': 10}])['result']

    def get_categories(self):
        return \
            self.mongo.db[self.tenders].aggregate([{'$group': {"_id": {'name': "$IdKategorija"}, "y": {"$sum": 1}}},
                                                   {"$project": {"_id": 1, 'y': 1}}, {'$sort': {'y': -1}}])['result']

    def group_by_date(self):
        return self.mongo.db[self.tenders].aggregate(
            [
                {
                    "$project": {
                        'year': {'$substr': ["$DatumPoslednjeIzmene", 0, 4]},
                        'month':{'$substr': ["$DatumPoslednjeIzmene", 5, 2]},
                        "name": "$IdKategorija"
                    }
                },
                {
                    "$group":{
                        "_id":{
                            "month": "$month",
                            "name":"$name",
                            "year": "$year"
                        },
                        "count":{"$sum": 1}
                    }
                },
                {
                    "$sort":{
                        "month":-1
                    }
                }
            ]
        )
