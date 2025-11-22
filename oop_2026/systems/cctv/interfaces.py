from abc import ABC, abstractmethod


class VisualFeed(ABC):
    pass


class TextVision(VisualFeed):
    # representation of the vision in terms of str (text; can be 2d)
    @abstractmethod
    def get(self) -> str:
        pass


class ThreatLevel:
    # how serious the danger is
    def get_level(self) -> int:
        pass


class ThreatEvaluator:
    # allows to evaluate single TextVision into one of ThreatLevel
    @abstractmethod
    def evaluate(self, vision: TextVision) -> ThreatLevel:
        pass


class ThreatMonitor:
    # observes ThreatLevels over time
    @abstractmethod
    def append_vision(self, vision: TextVision):
        pass


class AlarmAction:
    # how to react to certain threats
    @abstractmethod
    def react(self, threat_level: ThreatLevel):
        pass
