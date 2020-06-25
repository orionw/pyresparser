from nltk.corpus import stopwords

# Omkar Pathak
NAME_PATTERN = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
NAME_PATTERN_THREE = [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}]

# Education (Upper Case Mandatory)
EDUCATION = [
            'BACHELOR', 'B.E.', 'B.E', 'BS', 'B.S', 'M.E',
            'M.E.', 'M.S.', 'M.S', 'BTECH', 'MTECH', "MASTER", "MASTERS",
            "PHD", "PH.D.", "P.H.D.", "DOCTORATE",
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
        ]

SCHOOL_KEYWORDS = ['Hospital', 'University', 'Institute', 'School', 'School', 'Academy', "Center", "College"]

NOT_ALPHA_NUMERIC = r'[^a-zA-Z\d]'

NUMBER = r'\d+'

# For finding date ranges
MONTHS_SHORT = r'''(jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)
                   |(aug)|(sep)|(oct)|(nov)|(dec)'''
MONTHS_LONG = r'''(january)|(february)|(march)|(april)|(may)|(june)|(july)|
                   (august)|(september)|(october)|(november)|(december)'''
MONTH = r'(' + MONTHS_SHORT + r'|' + MONTHS_LONG + r')'
YEAR = r'(((20|19)(\d{2})))'

STOPWORDS = set(stopwords.words('english'))

RESUME_SECTIONS_PROFESSIONAL = [
                    'experience',
                    'education',
                    'interests',
                    'professional experience',
                    'publications',
                    'skills',
                    'certifications',
                    'objective',
                    'career objective',
                    'summary',
                    'leadership'
                ]

RESUME_SECTIONS_GRAD = [
                    'awards',
                    'accomplishments',
                    'experience',
                    'education',
                    'interests',
                    'projects',
                    'professional experience',
                    'publications',
                    'skills',
                    'certifications',
                    'objective',
                    'career objective',
                    'summary',
                    'leadership'
                ]
