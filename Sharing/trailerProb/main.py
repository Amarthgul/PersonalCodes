import pandas as pd
import matplotlib.pyplot as plt
import pickle

cached = True
if not cached:
    route = pd.read_excel("route.xlsx")
    location = pd.read_excel("worldcities.xlsx")
    with open("cities.pckl", "wb") as f:
        pickle.dump((route, location), f)
else:
    with open("cities.pckl", "rb") as f:
        route, location = pickle.load(f)

class worldCities():
    def __init__(self, cachedPath = ""):
        self.cachePath = cachedPath
        self.__readID = False
        self.__readCountry = True
        self.__readISO = False
        self.__data = self.readCities()


    def readCities(self, turnToDataframe = False, cacheData = False):
        if self.cachePath != "":
            with open(self.cachePath, "rb") as f:
                cities = pickle.load(f)
                return cities;

        #names = ["city_ascii", "lat", "lng"]
        cities = {}
    
        for index, row in location.iterrows():
            currenrName = row["city_ascii"].lower().replace(" ", "")
            cities[currenrName] = {}
            cities[currenrName]["latitude"] = row["lat"]
            cities[currenrName]["longtitude"] = row["lng"]
            if self.__readID:
                cities[currenrName]["ID"] = row["id"]
            if self.__readCountry:
                cities[currenrName]["country"] = row["country"]
            if self.__readISO:
                cities[currenrName]["ISO2"] = row["iso2"]
                cities[currenrName]["ISO3"] = row["iso3"]

        if cacheData:
            with open("cache.pckl", "wb") as f:
                pickle.dump(cities, f)

        if turnToDataframe:
            return pd.DataFrame(cities)
        return cities;

    def getCityLoc(self, name = "Columbus"):
        name = name.lower().replace(" ", "")
        lat = self.__data[name]["latitude"]
        lng = self.__data[name]["longtitude"]
        return lng, lat


def plotCities():
    cities = worldCities()

    plt.style.use(u'ggplot')
    for i, row in route.iterrows():
        ori = cities.getCityLoc(row["Origin"])
        des = cities.getCityLoc(row["Destination"])
        plt.plot([ori[0], des[0]], [ori[1], des[1]], label = "Index " + str(i))

    plt.xlabel("Longitude"); plt.ylabel("Latitude")
    plt.legend()
    plt.show()


#=================================================
'''============================================'''

def main():
    plotCities()
    #pass

if __name__ == "__main__":
    main()
