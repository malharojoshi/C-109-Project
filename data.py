import pandas as pd
import csv
import statistics

df=pd.read_csv("data.csv")
reading_list=df["reading score"].to_list()


reading_mean=statistics.mean(reading_list)

reading_median=statistics.median(reading_list)


reading_mode=statistics.mode(reading_list)


print("Mean, Median, and Mode of Reading Score is {}, {}, and {} respectively".format(reading_mean,reading_median,reading_mode))

reading_stdd=statistics.stdev(reading_list)


reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean-reading_stdd, reading_mean+reading_stdd
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean-(2*reading_stdd), reading_mean+(2*reading_stdd)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean-(3*reading_stdd), reading_mean+(3*reading_stdd)



reading_list_of_data_within_1_std_deviation = [
    result for result in reading_list if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end
    ]
reading_list_of_data_within_2_std_deviation = [
    result for result in reading_list if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end
    ]
reading_list_of_data_within_3_std_deviation = [
    result for result in reading_list if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end
    ]

print("{}% of data for Reading Score lies within 1 standard deviation".format(len(reading_list_of_data_within_1_std_deviation)*100.0/len(reading_list)))
print("{}% of data for Reading Score lies within 2 standard deviation".format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(reading_list)))
print("{}% of data for Reading Score lies within 3 standard deviation".format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(reading_list)))
