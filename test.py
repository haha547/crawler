urllist = [
    "http://ecampus.nqu.edu.tw/eCampus3P/Learn/stu_course_default.aspx?CourseId=514bca90-541a-4c19-815b-060d9651e120&Role=Student",
    "http://ecampus.nqu.edu.tw/eCampus3P/Learn/stu_course_default.aspx?CourseId=28ff4a92-469b-43ac-aeac-6e5a79074c3f&Role=Student",
    "http://ecampus.nqu.edu.tw/eCampus3P/Learn/stu_course_default.aspx?CourseId=c6962594-197f-457e-ae7f-8bc8b6b3025c&Role=Student",
    "http://ecampus.nqu.edu.tw/eCampus3P/Learn/stu_course_default.aspx?CourseId=0c317730-6ffa-40c2-a9ef-936d829af06e&Role=Student",
    "http://ecampus.nqu.edu.tw/eCampus3P/Learn/stu_course_default.aspx?CourseId=a14b6191-b24f-4f7e-9242-237f91187d84&Role=Student",
    "http://ecampus.nqu.edu.tw/eCampus3P/Learn/stu_course_default.aspx?CourseId=7f1d3fc5-c879-4032-952b-788465c84e1f&Role=Student",
    "http://ecampus.nqu.edu.tw/eCampus3P/Learn/stu_course_default.aspx?CourseId=c31374e9-0803-4a19-ba73-2aeae9dfbd9e&Role=Student",
    "http://ecampus.nqu.edu.tw/eCampus3P/Learn/stu_course_default.aspx?CourseId=efba9ec8-22e1-407b-a307-8ee9f89ea34e&Role=Student",
    "http://ecampus.nqu.edu.tw/eCampus3P/Learn/stu_course_default.aspx?CourseId=b17bbe45-3686-454a-9b9e-ec94d0cbd28a&Role=Student",
    "http://ecampus.nqu.edu.tw/eCampus3P/Learn/stu_course_default.aspx?CourseId=b805c896-2752-46a0-b921-afe452f790b2&Role=Student"
]
courseName = [
    "數位邏輯",
    "資料結構",
    "計算機結構",
    "網站架設實務",
    "智慧型行動裝置軟體設計",
    "資料探勘導論",
    "專業實習(一)",
    "終身學習與知識管理",
    "西洋歌曲賞析",
    "體育"
]



new_dict = dict(zip(urllist, courseName))
for i in new_dict:
    print(i,new_dict[i])