from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

careers = {
    "ai-ml": {
        "title": "AI / Machine Learning Engineer",
        "description": "Build intelligent systems that learn from data",
        "duration": "12-18 months",
        "salary": "8-25 LPA",
        "steps": [
            {
                "title": "Python Basics",
                "duration": "1 month",
                "topics": ["Variables", "Loops", "Functions", "OOP"],
                "links": [
                    {"name": "🎥 Python Full Course - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=UrsmFxEIp5k"},
                    {"name": "🎥 Python Basics - CampusX (Hindi)", "url": "https://www.youtube.com/playlist?list=PLKnIA16_Rmvb1RYR-iTA_hzckhdONtSW4"}
                ]
            },
            {
                "title": "Mathematics for AI",
                "duration": "1 month",
                "topics": ["Linear Algebra", "Statistics", "Probability", "Calculus basics"],
                "links": [
                    {"name": "🎥 Statistics - CampusX (Hindi)", "url": "https://www.youtube.com/watch?v=tPhzDKjQBpo&list=PLKnIA16_RmvbVrE0eZO2bCaFln6jaNq-1"},
                    {"name": "🎥 Linear Algebra - CampusX (Hindi)", "url": "https://www.youtube.com/watch?v=e9h-ZZ_ahRg&list=PLKnIA16_RmvYu0fS_RuIB2eTbJcTFdrAA"}
                ]
            },
            {
                "title": "Machine Learning",
                "duration": "2 months",
                "topics": ["Supervised Learning", "Unsupervised Learning", "Scikit-learn", "Model Evaluation"],
                "links": [
                    {"name": "🎥 100 Days of ML - CampusX (Hindi)", "url": "https://www.youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH"},
                    {"name": "🎥 ML Full Course - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=UrsmFxEIp5k"}
                ]
            },
            {
                "title": "Deep Learning",
                "duration": "2 months",
                "topics": ["Neural Networks", "TensorFlow", "Keras", "CNN", "RNN"],
                "links": [
                    {"name": "🎥 Deep Learning - CampusX (Hindi)", "url": "https://www.youtube.com/watch?v=wQ8BIBpya2k"},
                    {"name": "🎥 Neural Networks - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=aircAruvnKk"}
                ]
            },
            {
                "title": "Generative AI & LLMs",
                "duration": "2 months",
                "topics": ["ChatGPT API", "LangChain", "Prompt Engineering", "RAG"],
                "links": [
                    {"name": "🎥 Generative AI - CampusX (Hindi)", "url": "https://www.youtube.com/watch?v=G2fqAlgmoPo"},
                    {"name": "🎥 LangChain Hindi Tutorial - CampusX", "url": "https://www.youtube.com/watch?v=aywZrzNaKjs"}
                ]
            }
        ]
    },
    "devops": {
        "title": "DevOps Engineer",
        "description": "Bridge the gap between development and operations",
        "duration": "10-14 months",
        "salary": "7-22 LPA",
        "steps": [
            {
                "title": "Linux Basics",
                "duration": "3 weeks",
                "topics": ["Terminal Commands", "File System", "Permissions", "Shell Scripting"],
                "links": [
                    {"name": "🎥 Linux Full Course - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=iwolPf6kN-k"},
                    {"name": "🎥 Linux Tutorial - Apna College (Hindi)", "url": "https://www.youtube.com/watch?v=rowWJ0MntqU"}
                ]
            },
            {
                "title": "Git & GitHub",
                "duration": "2 weeks",
                "topics": ["Git basics", "Branching", "Pull Requests", "GitHub Actions"],
                "links": [
                    {"name": "🎥 Git & GitHub - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=gwWKnnCMQ5c"},
                    {"name": "🎥 Git & GitHub - Apna College (Hindi)", "url": "https://www.youtube.com/watch?v=Ez8F0nW6S-w"}
                ]
            },
            {
                "title": "Docker",
                "duration": "1 month",
                "topics": ["Containers", "Dockerfile", "Docker Compose", "Docker Hub"],
                "links": [
                    {"name": "🎥 Docker Full Course - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=3c-iBn73dDE"},
                    {"name": "🎥 Docker Tutorial - Hitesh Choudhary (Hindi)", "url": "https://www.youtube.com/watch?v=gAkwW2tuIqE"}
                ]
            },
            {
                "title": "Kubernetes",
                "duration": "2 months",
                "topics": ["Pods", "Deployments", "Services", "Helm", "Minikube"],
                "links": [
                    {"name": "🎥 Kubernetes - Kunal Kushwaha (Hindi)", "url": "https://www.youtube.com/watch?v=KVBON1lA9N8"},
                    {"name": "🎥 Kubernetes Full Course - TechWorld with Nana", "url": "https://www.youtube.com/watch?v=X48VuDVv0do"}
                ]
            },
            {
                "title": "CI/CD & GitHub Actions",
                "duration": "1 month",
                "topics": ["GitHub Actions", "Jenkins", "CI/CD Pipeline", "Automation"],
                "links": [
                    {"name": "🎥 DevOps Bootcamp - Kunal Kushwaha (Hindi)", "url": "https://www.youtube.com/playlist?list=PL9gnSGHSqcnoqBXdMwUTRod4Gi3eac2Ak"},
                    {"name": "🎥 GitHub Actions - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=R8_veQiYBjI"}
                ]
            }
        ]
    },
    "webdev": {
        "title": "Web Developer",
        "description": "Build websites and web applications",
        "duration": "8-12 months",
        "salary": "5-18 LPA",
        "steps": [
            {
                "title": "HTML & CSS",
                "duration": "1 month",
                "topics": ["HTML Tags", "CSS Styling", "Flexbox", "Grid", "Responsive Design"],
                "links": [
                    {"name": "🎥 HTML Full Course - Apna College (Hindi)", "url": "https://www.youtube.com/watch?v=HcOc7P5BMi4"},
                    {"name": "🎥 CSS Full Course - Apna College (Hindi)", "url": "https://www.youtube.com/watch?v=ESnrn1kAD4E"}
                ]
            },
            {
                "title": "JavaScript",
                "duration": "2 months",
                "topics": ["ES6+", "DOM Manipulation", "Fetch API", "Async/Await"],
                "links": [
                    {"name": "🎥 JavaScript Full Course - Apna College (Hindi)", "url": "https://www.youtube.com/watch?v=ajdRvxDWH4w"},
                    {"name": "🎥 JavaScript - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=UrsmFxEIp5k"}
                ]
            },
            {
                "title": "React.js",
                "duration": "2 months",
                "topics": ["Components", "Props", "State", "Hooks", "React Router"],
                "links": [
                    {"name": "🎥 React Full Course - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=RGKi6LSPDLU"},
                    {"name": "🎥 React - Apna College (Hindi)", "url": "https://www.youtube.com/watch?v=RwPhhU7RSSs"}
                ]
            },
            {
                "title": "Backend - Node.js",
                "duration": "2 months",
                "topics": ["Node.js", "Express.js", "REST APIs", "MongoDB"],
                "links": [
                    {"name": "🎥 Node.js - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=BLl32FvcdVM"},
                    {"name": "🎥 Full Stack Web Dev - Apna College (Hindi)", "url": "https://www.youtube.com/watch?v=RwPhhU7RSSs"}
                ]
            }
        ]
    },
    "cybersecurity": {
        "title": "Cybersecurity Engineer",
        "description": "Protect systems and networks from cyber attacks",
        "duration": "12-18 months",
        "salary": "6-20 LPA",
        "steps": [
            {
                "title": "Networking Basics",
                "duration": "1 month",
                "topics": ["TCP/IP", "DNS", "HTTP", "Firewalls", "VPN"],
                "links": [
                    {"name": "🎥 Networking Full Course - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=qiQR5rTSshw"},
                    {"name": "🎥 Computer Networks - Apna College (Hindi)", "url": "https://www.youtube.com/watch?v=IPvYjXCsTg8"}
                ]
            },
            {
                "title": "Linux for Security",
                "duration": "3 weeks",
                "topics": ["Kali Linux", "Terminal", "File Permissions", "User Management"],
                "links": [
                    {"name": "🎥 Linux - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=iwolPf6kN-k"},
                    {"name": "🎥 Kali Linux Full Course - Hindi", "url": "https://www.youtube.com/watch?v=lZAoFs75_cs"}
                ]
            },
            {
                "title": "Ethical Hacking",
                "duration": "3 months",
                "topics": ["Penetration Testing", "Metasploit", "Nmap", "Burp Suite"],
                "links": [
                    {"name": "🎥 Ethical Hacking - Apna College (Hindi)", "url": "https://www.youtube.com/watch?v=3Kq1MIfTWCE"},
                    {"name": "🎥 Ethical Hacking Full Course Hindi", "url": "https://www.youtube.com/watch?v=fNzpcB7ODxQ"}
                ]
            },
            {
                "title": "Certifications",
                "duration": "3 months",
                "topics": ["CompTIA Security+", "CEH", "OSCP", "CISSP"],
                "links": [
                    {"name": "🎥 CEH Course - Hindi", "url": "https://www.youtube.com/watch?v=hXSFdwCfh0Q"},
                    {"name": "🎥 Cybersecurity Roadmap - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=9Hd8QJmZQUc"}
                ]
            }
        ]
    },
    "datascience": {
        "title": "Data Scientist",
        "description": "Analyze data to find insights and build predictive models",
        "duration": "10-14 months",
        "salary": "7-20 LPA",
        "steps": [
            {
                "title": "Python & Statistics",
                "duration": "1 month",
                "topics": ["Python basics", "NumPy", "Pandas", "Statistics"],
                "links": [
                    {"name": "🎥 Python - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=UrsmFxEIp5k"},
                    {"name": "🎥 Pandas - CampusX (Hindi)", "url": "https://www.youtube.com/watch?v=kq9Vmg5d7Sk&list=PLKnIA16_RmvbR85fgbfVRKOiMokUKVupy"}
                ]
            },
            {
                "title": "Data Visualization",
                "duration": "3 weeks",
                "topics": ["Matplotlib", "Seaborn", "Plotly", "Tableau"],
                "links": [
                    {"name": "🎥 Matplotlib - CampusX (Hindi)", "url": "https://www.youtube.com/watch?v=CpPLLp3snK4&list=PLKnIA16_Rmvb-ToL3RQ_bwxG4_ND-0-DT"},
                    {"name": "🎥 Seaborn - CampusX (Hindi)", "url": "https://www.youtube.com/playlist?list=PLKnIA16_RmvbB1bFGjvS6a8T0mnqawejo"}
                ]
            },
            {
                "title": "Machine Learning",
                "duration": "2 months",
                "topics": ["Scikit-learn", "Regression", "Classification", "Clustering"],
                "links": [
                    {"name": "🎥 100 Days of ML - CampusX (Hindi)", "url": "https://www.youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH"},
                    {"name": "🎥 ML Roadmap - CampusX (Hindi)", "url": "https://www.youtube.com/watch?v=bPrmA1SEN2k"}
                ]
            },
            {
                "title": "SQL & Databases",
                "duration": "3 weeks",
                "topics": ["SQL basics", "Joins", "Aggregations", "PostgreSQL"],
                "links": [
                    {"name": "🎥 SQL Full Course - Apna College (Hindi)", "url": "https://www.youtube.com/watch?v=hlGoQC332VM"},
                    {"name": "🎥 SQL - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY"}
                ]
            }
        ]
    },
    "cloud": {
        "title": "Cloud Engineer",
        "description": "Design and manage cloud infrastructure",
        "duration": "10-14 months",
        "salary": "8-22 LPA",
        "steps": [
            {
                "title": "Cloud Basics",
                "duration": "2 weeks",
                "topics": ["What is Cloud", "IaaS PaaS SaaS", "Public Private Hybrid Cloud"],
                "links": [
                    {"name": "🎥 Cloud Computing - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=M988_fsOSWo"},
                    {"name": "🎥 Cloud Basics - Apna College (Hindi)", "url": "https://www.youtube.com/watch?v=RWgW-CgdIk0"}
                ]
            },
            {
                "title": "AWS Core Services",
                "duration": "2 months",
                "topics": ["EC2", "S3", "VPC", "IAM", "Lambda", "RDS"],
                "links": [
                    {"name": "🎥 AWS Full Course Hindi - Hitesh Choudhary", "url": "https://www.youtube.com/watch?v=ubCNZFXTFv4"},
                    {"name": "🎥 AWS for Beginners - CodeWithHarry (Hindi)", "url": "https://www.youtube.com/watch?v=k1RI5locZE4"}
                ]
            },
            {
                "title": "Terraform",
                "duration": "1 month",
                "topics": ["Infrastructure as Code", "Terraform basics", "Modules", "State Management"],
                "links": [
                    {"name": "🎥 Terraform Hindi - Kunal Kushwaha", "url": "https://www.youtube.com/watch?v=SLB_c_ayRMo"},
                    {"name": "🎥 Terraform Beginners - Hindi", "url": "https://www.youtube.com/watch?v=l5k1ai_GBDE"}
                ]
            },
            {
                "title": "AWS Certifications",
                "duration": "2 months",
                "topics": ["AWS Cloud Practitioner", "AWS Solutions Architect", "AWS DevOps"],
                "links": [
                    {"name": "🎥 AWS Certification Guide Hindi", "url": "https://www.youtube.com/watch?v=SOTamWNgDKc"},
                    {"name": "🎥 AWS Solutions Architect Hindi", "url": "https://www.youtube.com/watch?v=Ia-UEYYR44s"}
                ]
            }
        ]
    }
}

@app.route('/')
def home():
    return render_template('index.html', careers=careers)

@app.route('/career/<career_id>')
def career(career_id):
    if career_id in careers:
        return render_template('career.html', career=careers[career_id], career_id=career_id)
    return "Career not found", 404

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    results = {}
    for key, value in careers.items():
        if query in value['title'].lower() or query in value['description'].lower():
            results[key] = value
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)