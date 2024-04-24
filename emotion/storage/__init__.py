from storage.storage import JSONStorage
from datetime import datetime
from emotion.signals import Signal


storage = JSONStorage('dev.json')
StorageModifiedSignal = Signal(trace=True)
