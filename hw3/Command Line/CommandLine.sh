#!/bin/bash

# First we are going to merge to create the .tsv file we will be working with.
# The file was created with ">" just the names of each category we have and then we added all the course rows via ">>"
cat tsv/column_names.tsv > merged_courses.tsv
cat tsv/course_*.tsv >> merged_courses.tsv

# From now on we will use the command "awk -F '/t'" to make sure that the .tsv created is tabulated well and that you can navigate within the column.

### Country with the highest number of Master's degrees
# For the first question via "print $11" prints all the countries in the dataset, they are then put in order with "sort," duplicates removed, and a count done for each tamite "uniq -c.".
# They were then put in descending order based on the count just done with "sort -nr" and finally only the first row with country name and college number is extracted through "awk '{print $2 " " $3 " $1}' | head -n 1".
most_courses_country=$(awk -F'\t' '{print $11}' merged_courses.tsv | sort | uniq -c | sort -nr | awk '{print $2 " " $3 " " $1}' | head -n 1)
echo "Country that offers the most Master's Degrees: $most_courses_country"

### City with the highest number of Master's degrees
# The same commands listed and explained before are used here only difference takes into account column 10 which corresponds to cities.
most_courses_city=$(awk -F'\t' '{print $10}' merged_courses.tsv | sort | uniq -c | sort -nr | awk '{print $2 " " $1}' | head -n 1)
echo "City offers the most Master's Degrees: $most_courses_city"

### Number of colleges with part-time education
# In this other question, the command "$4 ~ /Part time/" is used to blind and select the rows that have the words "Part time" in the fourth column, the command "wc -l" is used to count the rows obtained.
num_part_time_colleges=$(awk -F'\t' '$4 ~ /Part time/ {print $2}' merged_courses.tsv | sort | uniq | wc -l)
echo "Number of colleges offer Part-Time education: $num_part_time_colleges"

### Percentage of courses in engineering
# As in the last question we look in the first column for rows that have this time "Engineering|Engineer" and that is, that have in their name the word "Engineering" or ("|") "Engineer"
# In this last question, I specifically used the command "printf \"%.2f\"" which goes to format the output to 2 decimal places,
# and I used "BEGIN{...}" which if I had not used it the calculation would have been performed for each line of the input file, resulting in incorrect behavior for the desired objective.
# This is because this command causes everything in the curly brackets to be executed before scrolling through all the rows.
engineering_courses=$(awk -F '\t' '$1 ~ /Engineering|Engineer/ {print}' merged_courses.tsv | wc -l)
percentage=$(awk "BEGIN {printf \"%.2f\", ($engineering_courses /6000) * 100}")
echo "Percentage of courses in Engineering: $percentage%"



