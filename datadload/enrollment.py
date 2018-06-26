import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("datCRDC2013_14.csv",encoding="Latin-1")
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    all_enrollment = data["total_enrollment"].sum()
    races =["HI","AM","AS","HP","BL","WH","TR" ]
    results ={}
    
    for race in races:
       results["SCH_ENR_{0}_M".format(race)] = float("{0:.3}".format((data["SCH_ENR_{0}_M".format(race)].sum())/all_enrollment))
       results["SCH_ENR_{0}_F".format(race)] = float("{0:.3}".format((data["SCH_ENR_{0}_F".format(race)].sum())/all_enrollment))


print(results)
