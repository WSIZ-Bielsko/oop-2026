from oop_2026.systems.cctv.interfaces import TextVision, ThreatLevel, ThreatEvaluator


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


class SimpleEvaluator(ThreatEvaluator):

    def evaluate(self, vision: TextVision) -> ThreatLevel:
        # implemen this method...
        # return level=1 if at least '**' are present in Vision
        # level=2 if ** are present in vision[:4]
        # else --> level=0
        pass


if __name__ == '__main__':
    vision1 = '      **          '
    vision2 = '   **             '
    vision3 = ' **               '
