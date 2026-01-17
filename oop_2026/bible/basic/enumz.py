from enum import Enum


class ExamStatus(str, Enum):
    INACTIVE = 'exam exists but is not activated'
    ACTIVE = 'exam can be started'
    IN_PROGRESS = 'exam is in progress'
    PAUSED = 'exam is paused'
    FINISHED = 'exam is finished'
    CANCELLED = 'exam was cancelled'


if __name__ == '__main__':
    current_status = ExamStatus.ACTIVE

    if current_status == ExamStatus.ACTIVE:
        print('exam is active')
        current_status = ExamStatus.PAUSED
