from oop_2026.systems.cctv.interfaces import TextVision, ThreatLevel, ThreatEvaluator, ThreatMonitor, AlarmAction


class OneDVision(TextVision):
    def __init__(self, line: str):
        self.line = line

    def get(self) -> str:
        return self.line


class TwoLevelThreat(ThreatLevel):
    def __init__(self, lv: int):
        self.lv = lv

    def get_level(self) -> int:
        return self.lv

    def __repr__(self):
        return f"ThreatLevel({self.lv})"

    def __ge__(self, other):
        return self.lv >= other.lv

    def __le__(self, other):
        return self.lv <= other.lv


class SimpleEvaluator(ThreatEvaluator):

    def evaluate(self, vision: TextVision) -> ThreatLevel:
        # implemen this method...
        # return level=1 if at least '**' are present in Vision
        # level=2 if ** are present in vision[:4]
        # else --> level=0
        level = 0
        line = vision.get()
        if '**' in line:
            level = 1
        if '**' in line[:4]:
            level = 2
        return TwoLevelThreat(level)


class AlertSentinel(ThreatMonitor):
    def __init__(self, evaluator: ThreatEvaluator):
        self.actions: list[tuple[ThreatLevel, AlarmAction]] = []
        self.evaluator = evaluator

    def append_vision(self, vision: TextVision):
        # either store the level associated with vision or...
        # just react to it
        current_level = self.evaluator.evaluate(vision)
        for level, action in self.actions:
            if current_level >= level:
                action.react(current_level)

    def register_alarm(self, level: ThreatLevel, action: AlarmAction):
        self.actions.append((level, action))


class LigthOnAction(AlarmAction):
    def react(self, threat_level: ThreatLevel):
        print("Ligth on!")


class SirenAction(AlarmAction):
    def react(self, threat_level: ThreatLevel):
        print("########### Siren! ##########")


if __name__ == '__main__':
    vision0 = '      *           '
    vision1 = '      **          '
    vision2 = '   **             '
    vision3 = ' **               '

    evaluator = SimpleEvaluator()
    print(evaluator.evaluate(OneDVision(vision1)))
    print(evaluator.evaluate(OneDVision(vision2)))
    print(evaluator.evaluate(OneDVision(vision3)))

    monitor = AlertSentinel(evaluator)
    monitor.register_alarm(TwoLevelThreat(1), LigthOnAction())
    monitor.register_alarm(TwoLevelThreat(2), SirenAction())

    print('---')
    monitor.append_vision(OneDVision(vision0))
    print('---')
    monitor.append_vision(OneDVision(vision1))
    print('---')
    monitor.append_vision(OneDVision(vision2))
    print('---')
    monitor.append_vision(OneDVision(vision3))
    print('---')
