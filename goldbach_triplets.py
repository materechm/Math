import csv
import math

class PrimeManager:
    def __init__(self, fileName, path, path_1mod6, path_5mod6):
        self.fileName = fileName
        self.primes = []
        self.triplets = []
        self.relationships = {}
        self.path = path
        self.path_1mod6 = path_1mod6
        self.path_5mod6 = path_5mod6

    def load_data_from_csv(self):
        read_file = open(self.fileName, 'rU')
        reader = csv.reader(read_file, delimiter=',')
        for row in reader:
            if not row:
                continue
            for x in row:
              self.primes.append(x)
        read_file.close()

    def create_triplets(self):
      for p in self.primes:
        p_2 = 2*int(p)
        s = 0
        while s < int(p)-1:
          s += 2
          p = int(p)
          p_a = p - s
          p_b = p + s
          if str(p_a) in self.primes and str(p_b) in self.primes:
              if p_a + p_b == p_2:
                print (p_a, p, p_b)
                self.triplets.append((p_a, p, p_b))
                p_a = str(p_a)
                p_b = str(p_b)
                p = str(p)
                group = self.relationships.setdefault(p_a, set())
                group.add(p)
                group = self.relationships.setdefault(p, set())
                group.add(p_b)


    def create_csv(self):
        print self.relationships
        for key in self.relationships:
            write_file = open(self.path, 'a')
            write_file.write(key)
            for x in self.relationships[key]:
                write_file.write('%s,' %x)
            write_file.write("\n")
            write_file.close()
            if int(key) % 6 == 1:
                write_file_1mod = open(self.path_1mod6, 'a')
                write_file_1mod.write(key)
                for x in self.relationships[key]:
                    write_file_1mod.write('%s,' %x)
                write_file_1mod.write("\n")
                write_file_1mod.close()
            if int(key) % 6 == 5:
                write_file_5mod = open(self.path_5mod6, 'a')
                write_file_5mod.write(key)
                for x in self.relationships[key]:
                    write_file_5mod.write('%s,' %x)
                write_file_5mod.write("\n")
                write_file_5mod.close()

def main():
    fileName = "/Users/mtchavez/Downloads/primes.csv" #location of file containing primes
    path = "/Users/mtchavez/Documents/prime_relationships.csv" #path to prime relationships file
    path_1mod6 = "/Users/mtchavez/Documents/prime_relationships1Mod6.csv"
    path_5mod6 = "/Users/mtchavez/Documents/prime_relationships5Mod6.csv"
    pm = PrimeManager(fileName, path, path_1mod6, path_5mod6)
    pm.load_data_from_csv()
    pm.create_triplets()
    pm.create_csv()

main()
