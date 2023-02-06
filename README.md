# **Surfs Up Analysis**

## *Overview of Analysis:*
    -The purpose of this challenge was to use SQLAlchemy to query a SQLite database in order to analyze the weather data that it contained.
    -The purpose of this analysis was to uncover weather trends from Oahu to help determine if a surf/ice cream shop business would be profitable year-round.

## *Results:*
    -From this analysis, it was determined that the average temperature in June is 74.9 degrees.
    -From this analysis, it was also determined that the average temperature in Decemeber is 71.0 degrees.
    -In this analysis, it was also detemined that the temperature ranged from 64.0 to 85.0 degrees in the month of June.
    -In this analysis, it was also determined that the temperatue ranged from 56.0 to 83.0 degrees in the month of December.
    
![June Temps Summary Stats](/Resources/june_temps.png)

![Dec Temps Summary Stats](/Resources/dec_temps.png)
    
## *Summary:*
    -This analysis can conclude that the temperatures between the months of June and Decemeber are relatively similar and therefore, the buiness would likely be profitable year round based off temperature alone. The average temperature only difference by about 4 degrees. Additionally, the highs differed only by 2 degrees while the lows differed by 8 degrees.
    -Further analysis should be done, as there are other weather factors that could impact the sustainablity of the business year round.
            -One additional query that could be completed to help with this analysis would be of the precipitation data for the months of June and Decemeber. This will provide further information of the weather differences between these two months to support or oppose the sustanability of the buisness year round.
                -Example of June: results = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 6).all()
            -Another query that could contribute to this analysis would be of the elevation of the different stations. The elevation of the different stations could provide infomation on the weather differences at these different elevations, within these months, and could ultimately help to guide where the location, and at what elevation, the business should be opened in.
                -Example of December: results = session.query(Measurement.date, Station.elevation).filter(extract('month', Measurement.date) == 12).all()
