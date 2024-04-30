from pyPhases import Phase

from pyPhasesRecordloader import RecordLoader

class Setup(Phase):
    def prepareConfig(self):
        # register custom vendor recordloaders
        RecordLoader.registerRecordLoader("RecordLoaderTest", "SleepHarmonizer.recordloaders")
        RecordLoader.registerRecordLoader("RecordLoaderDomino", "SleepHarmonizer.recordloaders")
        RecordLoader.registerRecordLoader("RecordLoaderAlice", "SleepHarmonizer.recordloaders")
