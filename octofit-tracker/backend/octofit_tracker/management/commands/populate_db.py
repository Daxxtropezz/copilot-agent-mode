from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

def populate():
    # Create Teams
    marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
    dc = Team.objects.create(name='DC', description='DC superheroes')

    # Create Users
    tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name)
    bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name)

    # Create Activities
    Activity.objects.create(user=tony.email, activity_type='run', duration=30, date='2025-10-01')
    Activity.objects.create(user=bruce.email, activity_type='cycle', duration=45, date='2025-10-02')

    # Create Workouts
    Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
    Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='medium')

    # Create Leaderboard
    Leaderboard.objects.create(team=marvel.name, points=100)
    Leaderboard.objects.create(team=dc.name, points=80)

if __name__ == '__main__':
    populate()
    print('Test data populated!')
