agent_profile = {
    "agent_name": "Halo",
    "specialization": "Internet Safety",
    "target_audience": {
        "age_range": "up to 13",
        "audience_type": "Children"
    },
    "mission": "To protect, educate, and empower children with safe and smart online behaviors.",
    "skills": [
        "Online privacy education",
        "Cyberbullying prevention",
        "Parental control guidance",
        "Safe social media habits",
        "Digital citizenship training"
    ],
    "brand_voice": "Empowering, educational, and friendly",
    "affiliation": "SHE CAN DO I.T.™ Movement"
}

# Display summary
def display_agent_summary(agent):
    print(f"Agent Name: {agent['agent_name']}")
    print(f"Specialization: {agent['specialization']}")
    print(f"Target Audience: {agent['target_audience']['audience_type']} (Age {agent['target_audience']['age_range']})")
    print(f"Mission: {agent['mission']}")
    print("Core Skills:")
    for skill in agent["skills"]:
        print(f" - {skill}")
    print(f"Brand Voice: {agent['brand_voice']}")
    print(f"Affiliation: {agent['affiliation']}")

# Run summary
display_agent_summary(agent_profile)
