
import anonymize
from load_data import dataset

anonymizeO = anonymize.Partition(5, 7, [0, 1, 2, 3, 4, 5, 6, 7])

anonymizedlist = anonymizeO.anonymize(dataset)

print(anonymizedlist)
