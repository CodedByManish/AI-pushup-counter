from pydantic import BaseModel

class WorkoutSession(BaseModel):
    user_id: int
    session_id: int
    exercises: list[str]  # List of exercise names
    duration: float  # Duration in minutes
    date: str  # Date of the session

class WorkoutStats(BaseModel):
    user_id: int
    total_sessions: int
    total_duration: float  # Total duration in minutes
    average_stats: dict[str, float]  # Average stats per session

class FormAnalysis(BaseModel):
    user_id: int
    session_id: int
    exercise_name: str
    form_errors: list[str]  # List of detected form errors
    score: float  # Form score between 0 and 100
