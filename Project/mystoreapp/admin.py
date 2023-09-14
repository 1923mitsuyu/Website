from flask import Blueprint, redirect, url_for
from . import db
from .models import Category, Textbook, Order
import datetime

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dbseed')
def dbseed():
    category1 = Category(name='Conversation', image='3.jpeg')
    category2 = Category(name='Examination', image='8.jpeg')
    category3 = Category(name='Grammar', image='9.jpeg')
    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.commit()
    except:
        return 'There was an issue adding the cities in dbseed function'
    
    # t1~t6 top selling 
    # t1 = Textbook(category_id=category2.id, image='1card.jpeg', price = 60.00,\
    #     date=datetime.datetime(2020, 5, 17),\
    #     name='CAMBRIDGE IELTS 17 ACADEMIC BOOK',\
    #     description= '''Authentic examination papers from Cambridge Assessment English provide perfect practice because they are EXACTLY like the real test. Inside IELTS 17 Academic with Answers with Audio you'll find FOUR complete examination papers plus details of the different parts of the test and the scoring system, so you can familiarise yourself with the Academic test format and practise your exam technique. Download the audio for the Listening tests, example Speaking test videos, answer keys with extra explanations and sample Writing answers (instructions on inner front cover), or access your audio and video directly via QR codes in the book.''')
    # t2 = Textbook(category_id=category2.id, image='2card.jpeg', price=58.95,\
    #     date=datetime.datetime(2020, 2, 1),\
    #     name='CAMBRIDGE IELTS 16 ACADEMIC BOOK',\
    #     description= '''Authentic examination papers from Cambridge Assessment English provide perfect practice because they are EXACTLY like the real test. Inside IELTS 16 Academic with Answers with Audio you'll find FOUR complete examination papers plus details of the different parts of the test and the scoring system, so you can familiarise yourself with the Academic test format and practise your exam technique. Download the audio for the Listening tests, example Speaking test video, answer keys with extra explanations and sample Writing answers (instructions on inner front cover), or access your audio and video directly via QR codes in the book.''')
    # t3 = Textbook(category_id=category2.id, image='3card.jpeg', price=62.33,\
    #     date=datetime.datetime(2020, 3, 10),\
    #     name='The Official Cambridge Guide to IELTS',\
    #     description= '''Perfect for students at band 4.0 and above, this study guide has EVERYTHING you need to prepare for IELTS Academic or General Training. Understand the test and improve your score with advice, tips and clear explanations. Exercises cover every question type, so you choose what to practise. Develop test-taking strategies with EIGHT official practice tests – the first one with step-by-step guidance. Audio for the listening exercises and practice tests, videos of the Speaking test are on the DVD-ROM. Alternatively download them all with The Official Cambridge Guide to IELTS App.''')
    # t4 = Textbook(category_id=category2.id, image='4card.jpeg', price=48.75,\
    #     date=datetime.datetime(2020, 8, 1),\
    #     name='Official Guide to the Toefl Test (Official Guide to the Toefl Ibt)',\
    #     description= '''This Official Guide to the TOEFL Test is the best, most reliable guide to the test that is used around the world to assess foreign applicants to U.S. and Canadian universities for English proficiency. It includes real TOEFL questions for practice, as well as explanations of every section of the test and information on what is expected for every speaking and writing task. You will learn how to construct a good answer and how to integrate speaking, listening, and writing skills to demonstrate college-level English proficiency. The accompanying CD-ROM provides three authentic TOEFL iBT practice tests just like the one you will encounter on test day.''')                
    # t5 = Textbook(category_id=category3.id, image='5card.jpeg', price=52.80,\
    #     date=datetime.datetime(2020, 4, 20),\
    #     name='English Grammar in Use Fourth Edition',\
    #     description= '''English Grammar in Use with Answers, authored by Raymond Murphy, is the first choice for intermediate (B1-B2) learners and covers all the grammar required at this level. It is a self-study book with simple explanations and lots of practice exercises, and has helped millions of people around the world to communicate in English. It is also trusted by teachers and can be used as a supplementary text in classrooms.''')
    # t6 = Textbook(category_id=category1.id, image='6card.jpeg', price=25.75,\
    #     date=datetime.datetime(2021, 1, 2),\
    #     name='Practice Makes Perfect: English Conversation, Premium Third Editio',\
    #     description= '''Conversing comfortably in a new language can seem like a daunting task. This accessible guide will help you build the skills to communicate in English with confidence. The book is packed with crystal-clear explanations, numerous realistic examples, and dozens of engaging exercises to help you hone your conversation skills. You'll learn how to introduce yourself, make appointments, strike up conversations, and much more.''')
    
    # # Conversation Category 
    # t7 = Textbook(category_id=category1.id, image='11card.jpeg', price=24.19,\
    #     date=datetime.datetime(2020, 11, 1),\
    #     name='110 Real Life English Conversations: with AUDIO featuring 27 native speakers for ESL Learners & teachers',\
    #     description= 'This book is filled with fun and creative dialogues based on real life situations between real people. With the audio, we tried to create a diverse cast with different American English accents to give you a good representation of how people talk on a daily basis.')
    # t8 = Textbook(category_id=category1.id, image='12card.jpeg', price=23.55,\
    #     date=datetime.datetime(2020, 4, 1),\
    #     name='101 Easy English Conversations: Simple English Dialogues with Questions for ESL Beginners ',\
    #     description= 'Improve your English ability in a fun way with these 101 Easy English Conversations. These easy English conversations & questions are designed for beginner level ESL/EFL learners.')
    # t9 = Textbook(category_id=category1.id, image='10card.jpeg', price=26.58,\
    #     date=datetime.datetime(2020, 5, 17),\
    #     name='''Preston Lee's Conversation English Lesson 1 - 40 For Bulgarian Speakers (Australian Version)''',\
    #     description= '''This book is designed to help English learners begin speaking conversation English. It is also an excellent learning resource for reading and comprehension. Have fun and learn English the easy way. This book has been written for all ages, children and adults alike.''')
    # t10 = Textbook(category_id=category1.id, image='13card.jpeg', price=19.99,\
    #     date=datetime.datetime(2020, 6, 19),\
    #     name='Collins Easy Learning English Conversation: Book 1 [Second Edition]',\
    #     description= '''The home of trusted English learner's dictionaries for everyday language learning. An exciting addition to the Easy Learning range, Collins Easy Learning English Conversation: Book 1 is a unique guide to communicating in English. It has been specially designed for beginners who want to learn how to communicate successfully and with confidence in everyday situations, at work, or when travelling or studying.''')
    # t11 = Textbook(category_id=category1.id, image='14card.jpeg', price=24.57,\
    #     date=datetime.datetime(2020, 2, 24),\
    #     name='101 Conversations in Simple English: Short Natural Dialogues to Boost Your Confidence & Improve Your Spoken English',\
    #     description= 'You’ll be transported into a real-world story that unfolds between six characters, told by the people themselves in 101 authentic conversations. Over 15,000 words of real English, you’ll immerse yourself in a gripping drama and get an education in natural English in the process.')
    
    # # Examination Category 
    # t12 = Textbook(category_id=category2.id, image='15card.jpeg', price=66.15,\
    #     date=datetime.datetime(2020, 10, 10),\
    #     name='TOEFL IBT: With 8 Online Practice Tests Paperback – 7',\
    #     description= '''Barron's newest edition of TOEFL iBT has been fully updated to reflect the new TOEFL format and provides flexible study options and key skills review to help you study what you need to know for the test. You'll also get 8 full-length practice tests, 8 one-hour practice tests, four video lessons, online PowerPoint presentations, and online audio files for all the practice to help you feel prepared on test day.''')
    # t13 = Textbook(category_id=category3.id, image='16card.jpeg', price=24.94,\
    #     date=datetime.datetime(2020, 7, 7),\
    #     name='Vocabulary and Grammar for the TOEFL Test [Second Edition]',\
    #     description= 'Collins Vocabulary and Grammar for the TOEFL iBT® Test is designed to help students master the vocabulary and grammar that they require to get a high score in the TOEFL iBT test. This book also exposes students to the task types they will encounter in the test. There are tips and strategies for how to approach the various test tasks which will enable students to improve their skills, gain confidence, and achieve the score they need.')

    # # Grammar Category 
    # t14 = Textbook(category_id=category3.id, image='17card.jpeg', price=33.95,\
    #     date=datetime.datetime(2020, 7, 7),\
    #     name='Oxford Modern English Grammar',\
    #     description='''Oxford Modern English Grammar is Oxford's brand new and definitive guide to English grammar. This book has been written by a leading expert in the field, covers both British and American English, and makes use of authentic spoken and written examples. Arranged in four clear parts for ease of use, its comprehensive coverage ranges from the very basic to the most complex aspects of grammar, all of which are explained clearly yet authoritatively. This
    #     descriptive source of reference is invaluable for those with an interest in the English language, undergraduate and postgraduate students, and for anyone who would like a clear guide to English grammar and how it is used.''')
   
    # t15 = Textbook(category_id=category3.id, image='18card.jpeg', price=46.95,\
    #     date=datetime.datetime(2020, 7, 7),\
    #     name='Essential Grammar in Use with Answers',\
    #     description= '''Grammar in Use is the world's best-selling grammar series for learners of English. Essential Grammar in Use with Answers, authored by Raymond Murphy, is the first choice for elementary-level (A1-B1) learners and covers all the grammar required at this level. It is a self-study book with simple explanations and lots of practice exercises, and has helped millions of people around the world to communicate in English. It is also trusted by teachers and can be used as a supplementary text in classrooms.''')

    # t16 = Textbook(category_id=category3.id, image='19card.jpeg', price=36.01,\
    #     date=datetime.datetime(2020, 7, 7),\
    #     name='Advanced Grammar in Use with Answers',\
    #     description= '''Grammar in Use is the world's best-selling grammar series for learners of English. Advanced Grammar in Use with Answers, authored by Martin Hewings, is the first choice for advanced (C1-C2) learners of English. It is a self-study book with clear explanations and practice exercises, and has helped millions of learners improve their English communication skills. It is also trusted by teachers and can be used as a supplementary text in classrooms, or to support preparation for Cambridge Advanced, Proficiency and IELTS examinations.''')

    # t17 = Textbook(category_id=category3.id, image='20card.jpeg', price=29.13,\
    #     date=datetime.datetime(2020, 7, 7),\
    #     name='English Grammar For Dummies',\
    #     description= '''Grasping the intricacies of the English language doesn't need to be tricky, and this down-to-earth guide breaks everything down in ways that make sense―Revealing rules, tips, and tricks to eliminate confusion and gain clarity, English Grammar For Dummies gives you everything you need to communicate with confidence!''')

    # t18 = Textbook(category_id=category3.id, image='21card.jpeg', price=26.96,\
    #     date=datetime.datetime(2020, 7, 7),\
    #     name='English for Everyone English Grammar Guide: A comprehensive visual reference',\
    #     description= '''You could be puzzled by prepositions, confused by comparatives, or muddled over modals. Thankfully, this complete visual aid to everything in the English language sets you straight with a clear and concise format for easy understanding.''')

    # try:
    #     # db.session.add(t1)
    #     db.session.add(t2)
    #     db.session.add(t3)
    #     db.session.add(t4)
    #     db.session.add(t5)
    #     db.session.add(t6)
    #     db.session.add(t7)
    #     db.session.add(t8)
    #     db.session.add(t9)
    #     db.session.add(t10)
    #     db.session.add(t11)
    #     db.session.add(t12)
    #     db.session.add(t13)
    #     db.session.add(t14)
    #     db.session.add(t15)
    #     db.session.add(t16)
    #     db.session.add(t17)
    #     db.session.add(t18)
    #     db.session.commit()
    # except:
    #     return 'There was an issue adding a tour in dbseed function'

    return 'DATA LOADED'