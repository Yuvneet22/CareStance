academic_assessment_questions = [
    {
        "id": "AE1_Math_Logic",
        "question": "A shopkeeper offers a 'Buy 2 Get 1 Free' deal, while another offers a flat 33% discount. Which approach would you use to determine the better deal?",
        "options": [
            {"value": "a", "text": "Set up an algebraic equation to compare the effective price per unit.", "stream": "PCM"},
            {"value": "b", "text": "Analyze the profit margin and consumer psychology behind the offers.", "stream": "COMM"},
            {"value": "c", "text": "Estimate the value based on immediate need and practical utility.", "stream": "VOC"},
            {"value": "d", "text": "Consider the ethical implications of 'lure' pricing on low-income families.", "stream": "ARTS"}
        ],
        "correct_value": "a", # Math logic focus
        "mapped_streams": ["PCM", "COMM"]
    },
    {
        "id": "AE2_Physics_Applied",
        "question": "If you are asked to explain why a heavy truck takes longer to stop than a small car moving at the same speed, which concept feels most intuitive to you?",
        "options": [
            {"value": "a", "text": "Calculating Momentum and Kinetic Energy using mathematical formulas.", "stream": "PCM"},
            {"value": "b", "text": "Understanding the biological reaction time of the driver.", "stream": "PCB"},
            {"value": "c", "text": "The practical mechanical wear and tear on the braking system.", "stream": "VOC"},
            {"value": "d", "text": "The urban planning regulations and safety laws regarding heavy vehicles.", "stream": "ARTS"}
        ],
        "correct_value": "a",
        "mapped_streams": ["PCM"]
    },
    {
        "id": "AE3_Biology_Systems",
        "question": "When studying the human heart, which aspect of the lesson captures your interest the most?",
        "options": [
            {"value": "a", "text": "The complex biochemical exchange of oxygen and the anatomy of valves.", "stream": "PCB"},
            {"value": "b", "text": "The heart as a mechanical pump that follows fluid dynamics and pressure laws.", "stream": "PCM"},
            {"value": "c", "text": "The public health statistics and economic cost of heart disease in society.", "stream": "COMM"},
            {"value": "d", "text": "The symbolic representation of the heart in literature and cultural history.", "stream": "ARTS"}
        ],
        "correct_value": "a",
        "mapped_streams": ["PCB"]
    },
    {
        "id": "AE4_Chemistry_Matter",
        "question": "While observing a chemical reaction that changes color, what is your first academic thought?",
        "options": [
            {"value": "a", "text": "What is the balanced molecular equation and the electron shift?", "stream": "PCM"},
            {"value": "b", "text": "How can this reaction be used to test for toxins in a biological sample?", "stream": "PCB"},
            {"value": "c", "text": "How can this chemical be mass-produced and marketed cost-effectively?", "stream": "COMM"},
            {"value": "d", "text": "What are the safety protocols and hands-on steps to perform this safely?", "stream": "VOC"}
        ],
        "correct_value": "a",
        "mapped_streams": ["PCM", "PCB"]
    },
    {
        "id": "AE5_Social_Economics",
        "question": "If you were reading about the Industrial Revolution, which topic would you choose for a 500-word essay?",
        "options": [
            {"value": "a", "text": "The evolution of the steam engine and mechanical thermodynamics.", "stream": "PCM"},
            {"value": "b", "text": "The shift from barter systems to global trade and capital markets.", "stream": "COMM"},
            {"value": "c", "text": "The impact of urbanization on labor rights and social class structures.", "stream": "ARTS"},
            {"value": "d", "text": "The transition from handmade crafts to machine-operated assembly lines.", "stream": "VOC"}
        ],
        "correct_value": "b",
        "mapped_streams": ["COMM", "ARTS"]
    },
    {
        "id": "AE6_Data_Interpretation",
        "question": "You are given a graph showing a country's population growth vs. food production. What is your primary takeaway?",
        "options": [
            {"value": "a", "text": "The geometric vs. arithmetic progression of the data points.", "stream": "PCM"},
            {"value": "b", "text": "The ecological impact and the sustainability of the food chain.", "stream": "PCB"},
            {"value": "c", "text": "The future demand-supply gap and its effect on inflation.", "stream": "COMM"},
            {"value": "d", "text": "The government policies needed to prevent a humanitarian crisis.", "stream": "ARTS"}
        ],
        "correct_value": "c",
        "mapped_streams": ["COMM", "PCM"]
    },
    {
        "id": "AE7_Language_Analysis",
        "question": "When analyzing a famous speech, what do you focus on most?",
        "options": [
            {"value": "a", "text": "The logical consistency and factual accuracy of the arguments.", "stream": "PCM"},
            {"value": "b", "text": "The use of metaphors, tone, and emotional appeal to influence the audience.", "stream": "ARTS"},
            {"value": "c", "text": "The persuasive techniques used to pitch an idea or 'sell' a vision.", "stream": "COMM"},
            {"value": "d", "text": "The clarity of instructions and how to present the information effectively.", "stream": "VOC"}
        ],
        "correct_value": "b",
        "mapped_streams": ["ARTS"]
    },
    {
        "id": "AE8_Environmental_Science",
        "question": "To solve the problem of water scarcity in a village, which 'academic' route would you prefer taking?",
        "options": [
            {"value": "a", "text": "Designing a desalination plant using chemical engineering and physics.", "stream": "PCM"},
            {"value": "b", "text": "Studying local plant life and groundwater ecosystems to restore balance.", "stream": "PCB"},
            {"value": "c", "text": "Creating a community-funded cooperative to manage water taxes and distribution.", "stream": "COMM"},
            {"value": "d", "text": "Implementing rainwater harvesting systems using basic plumbing and construction.", "stream": "VOC"}
        ],
        "correct_value": "b",
        "mapped_streams": ["PCB", "PCM", "VOC"]
    },
    {
        "id": "AE9_Logical_Structures",
        "question": "Which of these school subjects feels the most 'effortless' for you to study for 2 hours straight?",
        "options": [
            {"value": "a", "text": "Mathematics or Physics (Solving problems/Derivations).", "stream": "PCM"},
            {"value": "b", "text": "Biology or Chemistry (Understanding life/Matter).", "stream": "PCB"},
            {"value": "c", "text": "Economics, Accounts, or Business Studies.", "stream": "COMM"},
            {"value": "d", "text": "History, Geography, or Literature.", "stream": "ARTS"}
        ],
        "correct_value": "n/a", # Interest based academic preference
        "mapped_streams": ["PCM", "PCB", "COMM", "ARTS"]
    },
    {
        "id": "AE10_Technical_Aptitude",
        "question": "In a computer science class, which part of the 'academic' process do you enjoy most?",
        "options": [
            {"value": "a", "text": "Writing the logic/algorithms and solving complex coding puzzles.", "stream": "PCM"},
            {"value": "b", "text": "Using software to design graphics, edit videos, or create art.", "stream": "ARTS"},
            {"value": "c", "text": "Learning how to assemble hardware, troubleshoot networks, or fix gadgets.", "stream": "VOC"},
            {"value": "d", "text": "Analyzing how data and apps can be used to run a digital business.", "stream": "COMM"}
        ],
        "correct_value": "a",
        "mapped_streams": ["PCM", "VOC"]
    },
    {
        "id": "PI1_Hobbies",
        "question": "What hobbies or activities do you enjoy the most in your free time?",
        "type": "open",
        "placeholder": "e.g. Photography, playing guitar, coding, gardening..."
    },
    {
        "id": "PI2_Extracurricular",
        "question": "Have you participated in any extracurricular activities (sports, arts, clubs, competitions, etc.)?",
        "type": "open",
        "placeholder": "e.g. School football team, state-level painting competition, debate club..."
    }
]

# Split for different assessment sections
section_a_questions = academic_assessment_questions[:4] # Core logic/science
section_b_questions = academic_assessment_questions[4:7] # Application/Data
section_c_questions = academic_assessment_questions[7:9] # Environment/Preference
section_d_questions = academic_assessment_questions[9:10] # Hands-on/Technical
section_e_questions = academic_assessment_questions[10:12] # Personal Interests

all_questions = {
    "Section A": {"title": "Section A: Logic & Foundational Science", "questions": section_a_questions},
    "Section B": {"title": "Section B: Applied Concepts & Analysis", "questions": section_b_questions},
    "Section C": {"title": "Section C: Interdisciplinary Interests", "questions": section_c_questions},
    "Section D": {"title": "Section D: Technical Skills & Vocational Path", "questions": section_d_questions},
    "Section E": {"title": "Section E: Personal Interests & Hobbies", "questions": section_e_questions}
}