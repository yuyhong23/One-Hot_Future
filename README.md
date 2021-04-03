# One-Hot Future

![Project Logo](Static/images/updated_logo.png)

https://one-hot-future-2021.herokuapp.com/

[Presentation Slides](https://docs.google.com/presentation/d/1QRUPwZ48Yx9f9POyFoYEypm0VHGm-jsNK4KMjPsEnD4/edit?usp=sharing)

## Data Analytics Team:

*[Elizabeth Leshuk](https://github.com/eleshuk): logo, data cleaning, machine learning, HTML/CSS/js, presentation slide template

*[Rob Orgain](https://github.com/roborgain1): HTML/CSS/js, analysis

*[Tara Madhyasta](https://github.com/Polaris-pixel): data collection, machine learning, flask, tableau

*[Yuying Hong](https://github.com/yuyhong23): project organization, data collection, data cleaning, machine learning, tableau, Heroku

*Everyone: project idea, presentation slides, support/debug

## Background:

With COVID vaccination in progress, societies are slowly reopening to a new kind of normality. It is also time for the world to refocus on climate change, one of the most urgent problems that we are facing on Earth!

Climate crisis has been getting worse as time goes by. Around the world in recent years, we have been experiencing increasing number of natural disasters at uncommon intensities that were highly destructive to our societies; such as the wildfires in California, US, hurricanes in Atlantic basin, US and South America, bushfires in Australia, sandstorms in Beijing, China, and the list goes on.

Carbon dioxide emitted as a byproduct from energy consumption is the principal contributor to global warming, and countries around the world have come together at the Paris Agreement in 2015 to tackle this global issue.

## Project Scope:

As a team, we were curious to find out how the world and selective countries/regions are doing to meet their emission targets. We were also interested in visualizing the average temperature change by the world, and selective countries/regions.

## Tools and Libraries

- Python
- Pandas
- Sklearn (Conda Environment: PythonAdv)
- Seaborn
- hvplot.pandas
- functools
- Matplotlib
- NumPy
- HTML/CSS/Bootstrap
- Flask
- Tableau (for Visualizations)
- Heroku (for App Deployment)

## Method:

We used [bp's](https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy/downloads.html)
energy consumption data from 1965 to 2019 (most recent year available) in machine learning to predict the energy consumption in 2020, 2030, 2040 and 2050, and then used the predicted energy consumption values in machine learning to predict the future emission level.

    - For energy consumption, we looked at all energy, nonrenewable energy (and each specific energy type), and renewable energy consumption.
    - We focus mainly on global trends and selective regions that are big players in turn of energy consumption and emission.
        - Global, China, US, EU, India
    - We chose the year 2020, 2030, 2040, and 2050 for predictions, because…
        - 2020 would give us insight on whether the predictions are logically reasonable
        - 2030 is the year that countries specified what their emission pledges are (https://treaties.un.org/Pages/ViewDetails.aspx?src=IND&mtdsg_no=XXVII-7-d&chapter=27&clang=_en) (https://docs.google.com/spreadsheets/d/1LtaBOv70pvXVPDgLUGtTKnSxofjfZy7jx06bTSaMaH4/pubhtml?gid=14385633&single=true)
        - 2040 would show us the progress before getting to 2050
        - 2050 is the year that most countries would have emission level close to 0

We used [NASA](https://climate.nasa.gov/vital-signs/global-temperature/)’s global temperature annual average anomaly data from 1965 to 2020 (most recent year available) in machine learning to predict the average temperature change in 2030, 2040 and 2050. We visualized [kaggle](https://www.kaggle.com/sevgisarac/temperature-change) annual average temperature change by countries in 2019.

## Analysis:

#### Energy Types Consumption:

In 2019, the top five non-renewable resources harnessed for energy from highest to lowest consumption include oil (194 exajoules), coal (158 exajoules), gas (142 exajoules), hydroelectric (38 exajoules), and nuclear (25 exajoules) energy, with renewable consumption (21 exajoules) being lower than any individual aforementioned resource the same year. Using machine learning to predict the consumption for each resource with data from 1965 to 2019 shows that energy consumption in 2050 will increase slightly in all non-renewable resources, but will increase exponentially in renewable resources at 296 exajoules, which is 14 times higher than in 2019. Renewable resource consumption is projected to be the leading resource consumed among all non-renewable and renewable resources at 28% of the total, with oil being the second highest consumed consisting of 24% of the total by 2050.

#### CO2 Emissions & Avg Temp Change:

CO2 emissions are projected to increase steadily with 34,000 million tonnes produced in 2019 and 45,600 million tonnes expected in 2050. From 1965 to 2019, the global average temperature has increased by around 1 degrees Celsius and is projected to increase by another .5 degrees Celsius by 2050 giving a total increase from 1965 to 2050 at 1.5 degrees Celsius.

#### Extra Notes:

- Official emission pledges are made for 2030 for the Paris Agreement
- US’s emission goal is by 2025, but for our project’s purpose, we used that emission goal as the 2030’s emission goal
- US filed the intent to leave the Paris Agreement in 2019, and officially left in 2020. With Biden as the new US president, US rejoins the Paris Agreement, but the official emission pledge has not been made yet
- 2040 emission goals are half of the emission pledges for 2030, we did that to see the progress trend better
- 2050 emission goals are set to zero for all for this project’s purpose
- China plans to peak its emission before 2030, so the emission trend predicted is likely to be inaccurate

## Conclusion:

#### Energy Consumption (Exajoules) and Emission (Million Tonnes)

Based on the predictions we made through machine learning, in order to meet the global emission goal, drastic measures are needed right now for CO2 emission to drop to the planned level by 2030.

Overall, most regions would need to work harder to achieve their emission pledges by 2030. 

Even though our predictions show some disappointing trends regarding nonrenewable energy consumption and emission, we need to point out that the exponential trends shown in the renewable energy consumption are some good news! 

In fact, our predictions for the nonrenewable energy consumption and emission did not factor in how the rise in renewable energy would lower the nonrenewable energy consumption and emission. Our predictions were solely based on the past data, which is likely to change drastically as countries around the world start to shift to renewable energy in recent years.

#### Average Temperature Change (Celcius)

Based on the predictions we made through machine learning, the world’s temperature change would rise to slightly below 1.5 celsius by 2050, which would meet the Paris Agreement goal, despite the fact that the temperature would continue to rise. 
