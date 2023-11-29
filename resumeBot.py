import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define patterns and corresponding responses
patterns = [
    (r"hi|hello|hey",
     "Hello! You're talking to Tyler's Resume Bot. How may I assist you with information about Tyler Howard?"),
    (r"how are you", "I'm a computer program here to provide information about Tyler Howard."),
    (r"bye|goodbye", "Goodbye! If you have more questions about Tyler, feel free to ask."),
    (r"what do you know about Tyler",
     "Tyler Howard is an IT Support Specialist based in Atlanta, GA. He is proficient in Java, SQL, and Python."),
    (r"tell me about Tyler's skills",
     "Tyler's key skills include data visualization, critical thinking, cybersecurity, and technical writing."),
    (r"tell me about Tyler's experience",
     "Tyler has worked as a Senior Help Desk Support Specialist at VIPdesk Connect, managing Wazuh and VMware Horizon DaaS. He also has experience at Blue Microphone, Logitech, Skullcandy, Luma, and Wandering WiFi."),
    (r"notable projects",
     "Tyler manages a YouTube channel focused on First Person View drones and designs websites using Weebly for freelance clients."),

    (r"what is Tyler's educational background",
     "Tyler is pursuing a Master's Degree in Information Technology at Southern New Hampshire University, with a target completion date in May 2025. He holds a Bachelor of Science in Computer Information Systems from Southern New Hampshire University."),

    (r"how does Tyler handle challenges",
     "Tyler excels in critical thinking and is adept at troubleshooting complex technical issues. He has a proven track record of providing effective solutions to challenges."),

    (r"tell me about Tyler's technical proficiency",
     "Tyler is highly proficient in using technology systems and tools such as Active Directory, Microsoft 365 Administration, Salesforce, Wazuh, VMware Horizon DaaS, Zendesk, Cisco Meraki, and Windows Server."),

    (r"what sets Tyler apart as a candidate",
     "Tyler's unique combination of technical expertise, communication skills, and dedication to providing exceptional support sets him apart as a valuable candidate. He consistently exceeds service level standards in virtual high-volume call center environments."),

    (r"how does Tyler contribute to process improvement",
     "Tyler actively contributes to process improvement initiatives by leveraging his technical skills and experience. He is dedicated to enhancing system functionality and performance."),

    (r"tell me about Tyler's coding portfolio",
     "Tyler has a coding portfolio showcasing his proficiency in Java, SQL, and Python. He enjoys learning new coding languages and applying his skills to various projects."),

    (r"thank you", "You're welcome! If you have more questions or need further information, feel free to ask."),

    # Add more patterns for specific queries
]


# Function to generate a response based on user input
def generate_response(user_input):
    doc = nlp(user_input.lower())

    # Check each pattern and respond if there is a match
    for pattern, response in patterns:
        if any(token.text.lower() in doc.text.lower() for token in nlp(pattern)):
            return response

    # Default response if no pattern is matched
    return "I'm sorry, I don't have information about that specific query."


# Introduction
print("Hi! You're talking to Tyler's Resume Bot. How can I help you today?")

# Main loop for chatbot interaction
while True:
    user_input = input("Recruiter: ")
    if user_input.lower() == "exit":
        break

    response = generate_response(user_input)
    print("Bot:", response)
