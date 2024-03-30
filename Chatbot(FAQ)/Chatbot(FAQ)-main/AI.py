
import google.generativeai as genai
import json

genai.configure(api_key="AIzaSyDdFQFmmBq6DoGzhkQiZRm_RVvYCAX8BlY")


def ai_function(request):
    try:
        if request.method == 'POST':
            #req_body = json.loads(request.body)
            #if (req_body['message'] != None):
            req_body = request.json  # Access request body directly using request.json
            if 'message' in req_body and req_body['message'] != '':
                model = genai.GenerativeModel('gemini-pro')
                chat = model.start_chat(history=[
                    {
                        'role': 'user',
                        'parts': ['What is Academic Calender of Rangsit University?'],
                    },
                    {
                        'role': 'model',
                        'parts': ["""RSU Academic Calendar
                                     Semester 1: August - December
                                     Semester 2: January - May
                                     Summer: June - July""",],
                    },
                    {
                        'role': 'user',
                        'parts': ['What are the admission requirements?'],
                    },
                    {
                        'role': 'model',
                        'parts': ["""Admission Requirements

                                    Undergraduate Academic Entry Requirements:

                                    Academic Entry Requirement:
                                    Completed Upper Secondary School (M.6 Certificate) or its equivalent as recognized by the Thai Ministry of Education, OR
                                    Completed High School Grade 12 (US System), OR
                                    Passed 5 subjects of Cambridge IGCSE or O-Level with a Grade C or above (British System), OR completed International Baccalaureate (IB) Diploma.
                                    English Language Requirement:
                                    English is the applicant’s first language, OR
                                    B2 level in the CEFR framework, OR
                                    IELTS (Academic) overall score of 5.5, OR
                                    TOEFL score: Paper-Based Test 500, Computer-Based Test 173, Internet-Based Test 60, OR
                                    CU-TEP Test equivalent score of 70 or other approved equivalents, OR
                                    Pass the Rangsit University International College (RIC) Placement Test.
                                    Postgraduate Academic Entry Requirements:
                                    International applicants must have completed an approved Bachelor's Degree or its equivalent as recognized by the Thai Ministry of Education.
                                    Foundation courses may be required if the undergraduate degree is not related to the program being applied for (e.g., Master of Education).
                                    Important Notes:
                                    Original documents or certified copies of original documents are required.
                                    Police clearance from the applicant's country of origin stating no previous criminal record or related offense is necessary.
                                    For applicants from the 54 African countries, additional requirements are needed, including sending original or certified copies of documents to Rangsit University.
                                    Certified documents require a statement on every page from an authorized person certifying them as true copies of the originals, along with their signature and designation/job title.
                                    For more information and detailed requirements, applicants can visit the Rangsit University website or contact the admissions office.""",],
                    },
                    {
                        'role': 'user',
                        'parts': [
                            "If the user asks about the schools from other countries or other schools in Thailand respond like this-> I apologize, but I am designed to provide information specifically about Rangsit University. If you have any inquiries regarding Rangsit University or need assistance with our services, feel free to ask, and I'll be happy to help."],
                    },
                    {
                        'role': 'model',
                        'parts': ["okay. Got it"],
                    },
                    {
                        'role': 'user',
                        'parts': [
                            "If the user asks about the not education or school related question please respond like this -> sorry i am designed to answer question related to Rangsit University"],
                    },
                    {
                        'role': 'model',
                        'parts': ["okay. Got it"],
                    },
                    {
                        'role': 'user',
                        'parts': ["What is the tuition fee at Rangsit University?"],
                    },
                    {
                        'role': 'model',
                        'parts': ["""Tuition fees at Rangsit University vary depending on the program, level of study, and whether the student is a domestic or international student. The university typically publishes detailed information about tuition and fees on its website, including annual tuition rates, additional fees (such as registration fees or laboratory fees), and payment deadlines. Students may also have the option to apply for scholarships, financial aid, or installment payment plans to help cover tuition costs."""],
                    },
                    {
                        'role': 'user',
                        'parts': ["Are there scholarships available for international students?"],
                    },
                    {
                        'role': 'model',
                        'parts': ["""Rangsit University offers scholarships and financial aid opportunities for both domestic and international students. 
                                  These scholarships may be merit-based, need-based, or awarded for specific achievements or talents. 
                                  The university typically provides information about available scholarships, eligibility criteria, a
                                  pplication procedures, and deadlines on its website or through the admissions office. 
                                  International students are encouraged to explore scholarship opportunities and apply for those for which they qualify to help offset 
                                  the cost of tuition and living expenses."""],
                    },
                    {
                        'role': 'user',
                        'parts': ["What facilities does Rangsit University provide for students?Is there support available for international students?"],
                    },
                    {
                        'role': 'model',
                        'parts': [
                            "Rangsit University is equipped with modern facilities designed to support student learning, research, and extracurricular activities. These facilities may include libraries stocked with academic resources and online databases, laboratories equipped with state-of-the-art equipment for scientific research and experimentation, computer centers with access to software and technology resources, sports facilities such as gymnasiums and athletic fields, student accommodation options, dining halls and cafeterias offering a variety of cuisines, and recreational areas for socializing and relaxation. Additionally, the university may offer specialized facilities tailored to specific academic programs or disciplines, such as studios for art and design students or simulation labs for medical students"],
                    },
                    {
                        'role': 'user',
                        'parts': ["Is there support available for international students?"],
                    },
                    {
                        'role': 'model',
                        'parts': ["""Rangsit University provides comprehensive support services for international students to help them adjust to campus life, navigate administrative procedures, and succeed academically. These support services may include assistance with visa and immigration processes, orientation programs to familiarize students with campus facilities and resources, academic advising to help students plan their course schedules and academic goals, language support services such as English language classes or tutoring, counseling services to address personal or academic concerns, and cultural integration programs to facilitate cross-cultural understanding and engagement. The university's international student services office serves as a central point of contact for international students seeking assistance and guidance."""],
                    },
                    {
                        'role': 'user',
                        'parts': [" Can I work while studying at Rangsit University?"],
                    },
                    {
                        'role': 'model',
                        'parts': [
                            """While traditional part-time employment options may be limited for international students in Thailand due to visa restrictions, there are alternative opportunities available. Rangsit University and other institutions may offer positions such as teaching assistantships, research assistants, or administrative roles to students. These positions allow students to gain valuable experience, contribute to academic departments, and earn 
                            supplemental income while studying. Teaching assistantships, for example, may involve assisting professors with course-related tasks, grading assignments, conducting tutorials, or providing academic support to students. These opportunities not only provide financial support but also enhance students' academic and professional development. Additionally, students may explore freelance or remote work options that do not require a work permit, such as online tutoring, content creation, or virtual assistance. It's important for students
                              to inquire about available positions through the university's career services office or academic departments and to ensure compliance with Thai immigration laws and regulations regarding work activities."""],
                    },
                    {
                        'role': 'user',
                        'parts': [" What is the campus life like at Rangsit University?"],
                    },
                    {
                        'role': 'model',
                        'parts': ["""Rangsit University offers a vibrant and dynamic campus life with numerous opportunities for students to engage in extracurricular activities, clubs,
                                   organizations, and events. The university's diverse student body contributes to a rich cultural and social atmosphere, where students can interact with 
                                  peers from different backgrounds and participate in various academic, cultural, and recreational activities. Campus facilities and amenities support
                                   student life, providing spaces for studying, socializing, and pursuing personal interests. Whether attending academic seminars, joining a sports team, participating 
                                  in cultural performances, or volunteering for community service projects, students at Rangsit University can enjoy a fulfilling and enriching campus experience.."""],
                    },
                    {
                        'role': 'user',
                        'parts': ["  How can I contact Rangsit University for more information?"],
                    },
                    {
                        'role': 'model',
                        'parts': [
                            """ Prospective students, current students, and other individuals seeking information about Rangsit University can contact the university through multiple channels. 
                            The university's official website serves as a primary source of information, offering details about academic programs, admissions procedures, tuition and fees, 
                            campus facilities, and contact information for various departments and offices. Additionally, individuals can reach out to the university via email, telephone, or 
                            in-person visits to specific offices or departments for personalized assistance. Rangsit University may also maintain active social media accounts and online forums where students and staff share information, 
                            announcements, and updates. By utilizing these communication channels, individuals can access the information and support they need to make informed decisions about academic pursuits, admissions, and campus life at Rangsit University."""],
                    },
                    {
                        'role': 'user',
                        'parts': [" How do I contact the university if I need more information?"],
                    },
                    {
                        'role': 'model',
                        'parts': [
                            """ Students can email rsuip@rsu.ac.th, call +662 997 2200 ext. 4012, 4019, or connect to social media like Facebook, Line, Instagram and Twitter, which are all available on this web site."""],
                    },
                ])
                response = chat.send_message(req_body['message'])
                return {
                    "success": True,
                    "message": response.text,
                }
            else:
                return {
                    "success": False,
                    "message": "Message is missing or empty!",
                }
        
    except:
        return {
            "success": False,
            "message": "Server error!",
        }
    


    