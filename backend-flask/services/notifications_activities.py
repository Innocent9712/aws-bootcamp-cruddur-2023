from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder


class NotificationsActivities:
  def run():
    now = datetime.now(timezone.utc).astimezone()
    segment = xray_recorder.begin_segment('notification_segment')
    # with xray_recorder.in_segment('notification_segment') as segment:
      # pass
    #   # Add metadata or annotation here if necessary
    segment.put_annotation("app.now", now.isoformat())
    # segment.put_metadata('key', {"sample": "value"}, 'namespace')
    results = [{
        'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Mr Buddy',
        'message': 'Cloud is fun!',
        'created_at': (now - timedelta(days=2)).isoformat(),
        'expires_at': (now + timedelta(days=5)).isoformat(),
        'likes_count': 5,
        'replies_count': 1,
        'reposts_count': 0,
        'replies': [{
            'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
            'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
            'handle':  'Worf',
            'message': 'Something ephemeral, maybe',
            'likes_count': 3005,
            'replies_count': 234,
            'reposts_count': 49,
            'created_at': (now - timedelta(days=2)).isoformat()
        }],
        },
        {
        'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
        'handle':  'Aligator Sensei',
        'message': 'There\'s somethin eerie about this',
        'created_at': (now - timedelta(days=7)).isoformat(),
        'expires_at': (now + timedelta(days=9)).isoformat(),
        'likes': 0,
        'replies': []
        },
        {
        'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
        'handle':  'Purple rain',
        'message': 'Look upon me, you must',
        'created_at': (now - timedelta(hours=1)).isoformat(),
        'expires_at': (now + timedelta(hours=12)).isoformat(),
        'likes': 0,
        'replies': []
        }
        ]
    # xray_recorder.end_segment()
    return results