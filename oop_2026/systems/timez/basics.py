from datetime import datetime, UTC, timedelta
from zoneinfo import ZoneInfo

if __name__ == '__main__':
    # tt = datetime.now().timestamp()
    tt = datetime.now()
    print(tt)
    print(tt.tzinfo)

    print('---'*10)
    tt = datetime.now(tz=UTC)
    print(tt)
    print(tt.tzinfo)

    tt += timedelta(hours=8)

    mar29 = datetime(2026, 3, 29, hour=0, minute=0, second=0, tzinfo=ZoneInfo('Europe/Warsaw'))
    utc29 = mar29.astimezone(UTC)
    for _ in range(10):
        print(f'warsaw: {mar29}, translated_utc: {mar29.astimezone(UTC)}, utc: {utc29}')
        mar29 += timedelta(hours=1)
        utc29 += timedelta(hours=1)

    riyadh = utc29.astimezone(ZoneInfo('Asia/Riyadh'))
    print(f'riyadh: {riyadh}')
    print('---'*10)
    print(utc29.isoformat())
    print(mar29.isoformat())
