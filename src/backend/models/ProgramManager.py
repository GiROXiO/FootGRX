from utils.dataStructures.DoubleLinkedCircularList import DoubleLinkedCircularList
from backend.models.season.Season import Season

class ProgramManager:
    def __init__(self):
        self.seasons = DoubleLinkedCircularList[Season]()