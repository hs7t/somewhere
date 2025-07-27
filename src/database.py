from tinydb import TinyDB, Query
from utils.time import getCurrentUTC, isoTimeString

def createStreakObject(
    name, 
    startTime=isoTimeString(getCurrentUTC),
    loggedUTCTimes=[isoTimeString(getCurrentUTC)],
    active=True
):
    return {
        'name': name,
        'startTime': startTime,
        'loggedUTCTimes': loggedUTCTimes,
        'active': active
    }

def insertStreak(db, streakObject):
    db.insert(streakObject)
