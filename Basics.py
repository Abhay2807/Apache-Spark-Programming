
# Creating a Dataframe in Databricks

from pyspark.sql import *

if __name__ == "__main__" :

    ipl_info=[

        ("Mumbai",5,"Rohit"),
        ("Delhi",0,"Pant"),
        ("Chennai",5,"Dhoni"),
        ("Kolkata",2,"Gambhir"),
        ("Hyderabad",1,"Warner")

    ]

    columns_ipl_info=["Team","Trophies","Captain"]

    df=spark.createDataFrame( ipl_info ,schema = columns_ipl_info )

    display(df)
