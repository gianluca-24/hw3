import csv
from bs4 import BeautifulSoup
from constants import NUM_PAGES, DIR_PATH, TSV_PATH

# this is a counter that allows me to index all the courses when creating the single .csv files
index = 0

# read the file containing the links
with open('link.txt','r') as file_link:
    for i in range(1,NUM_PAGES+1):
        # create new folder for the i-th page
        path = DIR_PATH + '/page_' + str(i)
        for x in range(15):
            #upload html file
            file_path = path + '/course_' + str(x) + '.html'
            html_content = open(file_path, 'r', encoding='utf-8')
            soup = BeautifulSoup(html_content, 'html.parser') # sue BeautifulSoup to parse HTML code
            # then, with the find(..) function I will find all the infos I need to build the dataset
            # course name
            title = soup.find(class_='text-white course-header__course-title')
            courseName = title.get('data-permutive-title') if title else '' 
            # uni name
            uni = soup.find(class_="course-header__institution text-white font-weight-light d-block d-md-inline")
            universityName = uni.text if uni else ''
            # faculty name
            fclt = soup.find(class_="course-header__department text-white font-weight-light d-block d-md-inline mt-2 mt-md-auto")
            facultyName = fclt.text if fclt else ''
            #isItFullTime
            ft = soup.find(class_="inheritFont concealLink text-decoration-none text-gray-600")
            isItFullTime = ft.text if ft else ''
            # description
            desc = soup.select('div.course-sections__content div#Snippet p')
            description = ''
            for d in desc:
                description += d.get_text(strip=True)
            # startDate
            date = soup.find(class_="key-info__content key-info__start-date py-2 pr-md-3 text-nowrap d-block d-md-inline-block")
            startDate = date.text if date else ''
            # fees
            f = soup.find(class_="course-sections course-sections__fees tight col-xs-24")
            fees = f.text.strip().replace('Fees\n\n','') if f else ''
            # modality
            mod = soup.find(class_="key-info__content key-info__qualification py-2 pr-md-3 text-nowrap d-block d-md-inline-block")
            modality = mod.text if mod else ''
            #duration
            d = soup.find(class_="key-info__content key-info__duration py-2 pr-md-3 d-block d-md-inline-block")
            duration = d.text if d else ''
            # city
            ct = soup.find(class_="card-badge text-wrap text-left badge badge-gray-200 p-2 m-1 font-weight-light course-data course-data__city")
            city = ct.text if ct else ''
            # country
            cntry = soup.find(class_="card-badge text-wrap text-left badge badge-gray-200 p-2 m-1 font-weight-light course-data course-data__country")
            country = cntry.text if cntry else ''
            #administration
            admin = soup.find(class_="card-badge text-wrap text-left badge badge-gray-200 p-2 m-1 font-weight-light course-data course-data__on-campus")
            administration = admin.text if admin else ''
            # url
            url = file_link.readline().strip()

            clmn = [courseName,universityName,facultyName,isItFullTime,description,startDate,fees,modality,duration,city,country,administration,url]

            #create tsv
            tsv_path = TSV_PATH + '/course_' + str(index) + '.tsv'
            tsv_file = open(tsv_path,'w', newline='', encoding='utf-8')
            tsv_writer = csv.writer(tsv_file, delimiter='\t')
            tsv_writer.writerow(clmn)

            html_content.close()
            tsv_file.close()

            index+=1

file_link.close()

# merge tsv files
tsv_path = 'C:\\Users\\Work\\Desktop\\Data science\\ADM\\HW3 ADM\\tsv\\course_'

# create the final .csv file
with open('master.tsv','a', newline='', encoding='utf-8') as master:
    writer = csv.writer(master, delimiter='\t')
    # initialize all the columns
    clmn = ['courseName','universityName','facultyName','isItFullTime','description','startDate','fees','modality','duration','city','country','administration','url']
    writer.writerow(clmn)
    # iterate over all the courses
    for i in range(6000):
        # open the i-th .csv file
        course_path = tsv_path + str(i) + '.tsv'
        course = open(course_path,'r',newline='', encoding='utf-8')
        reader = csv.reader(course,delimiter='\t') # create the reader
        # append the row
        row = next(reader, None)
        if row is not None: # check
            writer.writerow(row)
        course.close() # close file when I'm done with it

master.close() # close file