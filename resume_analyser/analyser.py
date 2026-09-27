from typing import List

# LangChain Imports
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2"
)

class ResumeAnalysis(BaseModel):
    skills: List[str] = Field(description="List of technical and soft skills found")
    experience_years: int = Field(description="Total years of experience")
    strengths: List[str] = Field(description="Key strengths of the candidate")
    weaknesses: List[str] = Field(description="Areas for improvement")
    ats_score: int = Field(description="ATS compatibility score out of 100")


class JobMatch(BaseModel):
    match_percentage: int = Field(description="Match percentage with job description")
    matching_skills: List[str] = Field(description="Skills that match the job")
    missing_skills: List[str] = Field(description="Skills required but missing")
    recommendations: List[str] = Field(description="Recommendations to improve match")


print("✅ Data Models defined.")

analyzer_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert resume analyst. Analyze the resume and provide detailed feedback."),
        ("human", "Resume Content:\n{resume}"),
    ]
)

# Connect Prompt to LLM with Structured Output
# This forces the LLM to return the Pydantic object, not just text
analyzer_chain = analyzer_prompt | llm.with_structured_output(ResumeAnalysis)

# --- DEMO DATA ---
sample_resume = """
Yash Jain - AI Software Engineer
Experience:
- 6 years as AI Developer at Tech Corp
- Built REST APIs using Python and Flask
- Managed PostgreSQL databases
Skills: Python, LangChain, LangGrapg, Flask, FastAPI, Docker, SQL, Git
Education: BE in Computer Science, 2020
"""

# Run the chain
analysis_result: ResumeAnalysis = analyzer_chain.invoke({"resume": sample_resume})

# Display Results
print(f"📊 ATS Score: {analysis_result.ats_score}")
print(f"✅ Skills: {analysis_result.skills}")
print(f"⚠️ Weaknesses: {analysis_result.weaknesses}")

matcher_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert recruiter. Compare the resume with the job description."),
        ("human", "Resume: {resume}\nJob Description: {job_description}"),
    ]
)

matcher_chain = matcher_prompt | llm.with_structured_output(JobMatch)

# --- DEMO DATA ---
job_description = """
Senior AI Developer
Requirements:
- 5+ years of experience in AI development
- Strong Python and FastAPI experience
- Database: SQL, MongoDB
- Cloud: AWS, Docker, Kubernetes
"""

# Run the chain
match_result: JobMatch = matcher_chain.invoke({"resume": sample_resume, "job_description": job_description})

# Display Results
print(f"📈 Match Percentage: {match_result.match_percentage}%")
print(f"❌ Missing Skills: {match_result.missing_skills}")
print(f"💡 Recommendations: {match_result.recommendations}")

improver_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a professional resume writer.
            Provide 3 specific bullet points to improve the resume based on the analysis.""",
        ),
        ("human", "Original Resume: {resume}\nAnalysis: {analysis}"),
    ]
)

# Simple StrOutputParser because we just want text back
improver_chain = improver_prompt | llm | StrOutputParser()

# Run the chain
suggestions = improver_chain.invoke(
    {
        "resume": sample_resume,
        "analysis": str(analysis_result),
    }  # Pass the previous a nalysis result
)

print("📝 Improvement Suggestions:\n")
print(suggestions)

# Memory Storage Dictionary
store = {}


def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# Define Chat Prompt with History Placeholder
coach_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a career coach. You remember the candidate's resume details. Be encouraging."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)

# Create the chain
coach_chain = coach_prompt | llm | StrOutputParser()

# Wrap chain with Message History
coach_with_memory = RunnableWithMessageHistory(
    coach_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

# --- INTERACTIVE DEMO ---
session_id = "user_123"

# 1. Seed the memory with context
initial_context = f"I have these skills: {analysis_result.skills}. My match score is {match_result.match_percentage}%."
coach_with_memory.invoke(
    {"input": initial_context},
    config={
        "configurable": {"session_id": session_id},
    },
)
print("🤖 Coach: Context received. How can I help?")

# 2. Ask follow-up questions
questions = [
    "What is the one skill I should learn next?",
    "How do I explain my missing experience in an interview?",
]

for q in questions:
    print(f"👤 User: {q}")
    response = coach_with_memory.invoke(
        {"input": q},
        config={
            "configurable": {"session_id": session_id},
        },
    )
    print(f"🤖 Coach: {response}")