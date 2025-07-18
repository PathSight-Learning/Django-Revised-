import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangophase1.settings')
django.setup()

from django.shortcuts import render
from .models import Field, Subfield, Skill, JobExample, LearningResource, RealWorldProject

fields = [
    {
        "name": "Software & Systems Development",
        "focus": "Building, testing, and maintaining software or systems",
        "subfields": [
            {
                "name": "Frontend Development",
                "common_job_titles": ["Frontend Developer", "Web Developer"],
                "key_tools_skills": ["HTML/CSS", "JavaScript", "React", "Vue"],
            },            {
                "name": "Backend Development",
                "common_job_titles": ["Backend Developer", "API Developer"],
                "key_tools_skills": ["Python", "Java", "Node.js", "SQL", "REST"],
            },
            {
                "name": "Full-Stack Development",
                "common_job_titles": ["Full-Stack Developer"],
                "key_tools_skills": ["Combination of frontend + backend"],
            },
            {
                "name": "Mobile App Development",
                "common_job_titles": ["iOS Developer", "Android Developer"],
                "key_tools_skills": ["Swift", "Kotlin", "Flutter", "React Native"],
            },
            {
                "name": "DevOps & Infrastructure",
                "common_job_titles": ["DevOps Engineer", "Site Reliability Engineer (SRE)"],
                "key_tools_skills": ["Docker", "Kubernetes", "CI/CD", "AWS"],
            },
        ],
        "jobs": [
            {
                "title": "Full Stack Developer",
                "description": "As a Full Stack Developer, you'll design, build, and maintain both the frontend and backend components of web applications. You'll work with databases, servers, APIs, and clients, taking ownership of the full development lifecycle.",
                "key_skills": [
                    "HTML/CSS",
                    "JavaScript",
                    "Frontend frameworks (React, Angular)",
                    "Backend frameworks (Node.js, Django)",
                    "SQL/NoSQL Databases",
                    "RESTful APIs and authentication",
                    "Version control (Git)"
                ],
                "learning_resources": [
                    {"name": "Full Stack Open (University of Helsinki)", "url": "https://fullstackopen.com/en/"},
                    {"name": "freeCodeCamp - Full Stack Certification", "url": "https://www.freecodecamp.org/learn/"},
                    {"name": "The Odin Project", "url": "https://www.theodinproject.com/paths/full-stack-javascript"}
                ],
                "real_world_projects": ["Blog platform with user authentication and CRUD operations", "Task Manager w/ real-time updates", "REST API for to-do list"]
            }
        ]
    },
    {
        "name": "Data, AI & Intelligence",
        "focus": "Building systems that analyze data or simulate intelligence",
        "subfields": [
            {
                "name": "Data Science",
                "common_job_titles": ["Data Scientist", "Data Analyst"],
                "key_tools_skills": ["Python", "Pandas", "SQL", "Jupyter", "Tableau"],
            },
            {
                "name": "Machine Learning & AI",
                "common_job_titles": ["ML Engineer", "AI Researcher"],
                "key_tools_skills": ["sci-kit learn", "TensorFlow", "PyTorch"],
            },
            {
                "name": "Data Engineering",
                "common_job_titles": ["Data Engineer", "ETL Developer"],
                "key_tools_skills": ["Spark", "Hadoop", "Airflow", "SQL"],
            },
            {
                "name": "Business Intelligence (BI)",
                "common_job_titles": ["BI Analyst", "Analytics Consultant"],
                "key_tools_skills": ["Power BI", "Looker", "Excel"]
            },
            {
                "name": "Natural Language Processing",
                "common_job_titles": ["NLP Engineer", "Computational Linguist"],
                "key_tools_skills": ["spaCy", "NLTK", "HuggingFace"]
            }
        ],
        "jobs": [
            {
                "title": "Machine Learning Engineer",
                "description": "As an ML Engineer, you'll build models that learn frmo data to make predictions or automate tasks - from fraud detection to recommendation engines. You'll work with data scientists to move models into production and ensure they work at scale.",
                "key_skills": [
                    "Python & libraries (NumPy, Pandas, scikit-learn)",
                    "Deep learning frameworks (PyTorch, TensorFlow)",
                    "Data wrangling and feature engineering",
                    "Math foundations (linear algebra, probability, optimization)",
                    "Git, Docker, APIs"
                ],
                "learning_resources": [
                    {"name": "Fast.ai Pratical Deep Learning", "url": "https://course.fast.ai/"},
                    {"name": "Coursera: Machine Learning by Andrew Ng", "url": "https://www.coursera.org/learn/machine-learning"},
                    {"name": "Kaggle Projects", "url": "https://www.kaggle.com/competitions"}
                ],
                "real_world_projects": ["spam email detector", "House price predictor", "Image classifier"]
            }
        ]
    },
    {
        "name": "Cybersecurity & Infrastructure",
        "focus": "Building systems that analyze data or simulate intelligence",
        "subfields": [
            {
                "name": "Cybersecurity",
                "common_job_titles": ["Security Analyst", "Penetration Tester"],
                "key_tools_skills": ["Kali Linux", "Wireshark", "Burp Suite"]
            },
            {
                "name": "Network & Cloud Security",
                "common_job_titles": ["Network Security Engineer"],
                "key_tools_skills": ["AWS/Azure security tools", "VPN", "firewalls"]
            },
            {
                "name": "Cloud Computing & Infratstructure",
                "common_job_titles": ["Cloud Engineer", "Systems Admin"],
                "key_tools_skills": ["AWS", "Azure", "Terraform", "Bash"]
            },
            {
                "name": "Blockchain & Web3",
                "common_job_titles": ["Blockchain Developer", "Smart Contract Engineer"],
                "key_tools_skills": ["Solidity", "Ethereum", "Web3.js"]
            }
        ],
        "jobs": [
            {
                "title": "Cybersecurity Analyst",
                "description": "As a Cybersecurity Analyst, you'll be the defender - monitoring networks, analyzing threats, and preventing cyberattacks. You may work in security operations centers (SOCs) or help protect sensitive systems and user data.",
                "key_skills": [
                    "Networking basics (TCP/IP, firewalls, VPN)",
                    "Security tools (Wireshark, Burp Suite, Nmap)",
                    "Threat modeling & penetration testing",
                    "Linux command line",
                    "Security certifications (CompTIA Security+, CEH)"
                ],
                "learning_resources": [
                    {"name": "TryHackMe Labs", "url": "https://tryhackme.com/"},
                    {"name": "MITRE ATT&CK Framework", "url": "https://attack.mitre.org/"},
                    {"name": "Coursera: IBM Cybersecurity Analyst Path", "url": "https://www.coursera.org/professional-certificates/ibm-cybersecurity-analyst"}
                ],
                "real_world_projects": ["Simulated phising email analysis", "Vulnerability scan report", "Linux log audit project"]
            }
        ]
    },
    {
        "name": "Research, Theory & Emerging Tech",
        "focus": "Innovation, theory, or academic/experimental CS work",
        "subfields": [
            {
                "name": "Computer Vision",
                "common_job_titles": ["CV Engineer", "Research Assistant"],
                "key_tools_skills": ["OpenCV", "TensorFlow", "YOLO"]
            },
            {
                "name": "Human-Computer Interaction (HCI)",
                "common_job_titles": ["UX Researcher", "Interaction Designer"],
                "key_tools_skills": ["Figma", "usability testing", "research methods"]
            },
            {
                "name": "Robotics",
                "common_job_titles": ["Robotics Engineer", "Embedded Systems Developer"],
                "key_tools_skills": ["ROS", "Arduino", "C++", "Python"]
            },
            {
                "name": "Quantum Computing",
                "common_job_titles": ["Quantum Researcher", "Quantum Software Developer"],
                "key_tools_skills": ["Qiskit", "IBM Q", "theoretical foundations"]
            },
            {
                "name": "Academia/Research",
                "common_job_titles": ["Research Assistant", "Ph.D. Student"],
                "key_tools_skills": ["Publications", "experimental methods", "LaTeX"]
            },
        ],
        "jobs": [
            {
                "title": "Quantum Comoputing Developer",
                "description": "As a Quantum Computing Developer, you'll build algorithms, simulations, and experimental software for quantum systems. You'll work at the intersection of physics, computer science, and mathematics to explore next-generation computing models, typically using quantum SDKs and simulators.",
                "key_skills": [
                    "Linear algebra and quantum mechanics fundamentals",
                    "Python and quantum programming frameworks (Qiskit, Cirq, or Braket)",
                    "Algorithm design (e.g. Grover's and Shor's algorithms)",
                    "Complex problem-solving and mathematical modeling",
                    "Familiarity with quantum information theory and gates"
                ],
                "learning_resources": [
                    {"name": "Qiskit Textbook (IBM)", "url": "https://qiskit.org/textbook/preface.html"},
                    {"name": "Quantum Computing for the Determined (YouTube series)", "url": "https://www.youtube.com/watch?v=JhHMJCUmq28"},
                    {"name": "edX - Quantum Computing Fundamentals by MIT", "url": "https://www.edx.org/professional-certificate/mitx-quantum-computing"},
                    {"name": "AWS Braket Developer Guide", "url": "https://docs.aws.amazon.com/braket/"},
                    {"name": "Cirq Documentation (Google)", "url": "https://quantumai.google/cirq"}
                ],
                "real_world_projects": []
            }
        ]
    }
]

# Django setup is already done above, models should work now

for field_data in fields:
    field, _ = Field.objects.get_or_create(name=field_data['name'])  # noqa

    for subfield_data in field_data['subfields']:
        subfield, _ = Subfield.objects.get_or_create(name=subfield_data['name'])  # noqa
        field.subfields.add(subfield)

        for job_data in field_data.get('jobs', []):
            job = JobExample.objects.create(  # noqa
                title=job_data['title'],
                description=job_data['description'],
                career_path=subfield
            )

            for skill_name in job_data['key_skills']:
                skill, _ = Skill.objects.get_or_create(name=skill_name)  # noqa
                job.skills.add(skill)

            for resource in job_data['learning_resources']:
                LearningResource.objects.create(  # noqa
                    name=resource['name'],
                    url=resource['url'],
                    job_example=job
                )

            for project in job_data['real_world_projects']:
                RealWorldProject.objects.create(  # noqa
                    name=project,
                    job_example=job
                )

print("Data loaded successfully")
from django.shortcuts import render
from .models import Field

def careerpaths_overview(request):
    fields = Field.objects.prefetch_related('subfields').all()
    return render(request, 'careerpaths/careerpaths.html', {'fields': fields})