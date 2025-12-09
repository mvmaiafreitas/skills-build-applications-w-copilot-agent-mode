from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(host='localhost', port=27017)
        db = client['octofit_db']

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email
        db.users.create_index([('email', 1)], unique=True)

        # Teams
        teams = [
            {'name': 'Marvel', 'description': 'Marvel Superheroes'},
            {'name': 'DC', 'description': 'DC Superheroes'}
        ]
        team_ids = db.teams.insert_many(teams).inserted_ids

        # Users
        users = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'Marvel'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'}
        ]
        db.users.insert_many(users)

        # Activities
        activities = [
            {'user': 'spiderman@marvel.com', 'type': 'run', 'distance': 5, 'duration': 30},
            {'user': 'ironman@marvel.com', 'type': 'cycle', 'distance': 20, 'duration': 60},
            {'user': 'wonderwoman@dc.com', 'type': 'swim', 'distance': 2, 'duration': 40},
            {'user': 'batman@dc.com', 'type': 'walk', 'distance': 3, 'duration': 50}
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'team': 'Marvel', 'points': 100},
            {'team': 'DC', 'points': 90}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {'name': 'Morning Cardio', 'suggestion': 'Run 5km'},
            {'name': 'Strength Training', 'suggestion': 'Pushups and Squats'}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
