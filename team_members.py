from fastapi import APIRouter
from supabase import create_client
from uuid import uuid4

team_router = APIRouter()

supabase_url = "https://eiselzqyfstbfttivvfh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVpc2VsenF5ZnN0YmZ0dGl2dmZoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4MjE4MDUsImV4cCI6MjA2NTM5NzgwNX0.6p75-Ye3zfMI4MilZrP6d2hat7G1PBtEArHHb9Uwupo"

db = create_client(supabase_url,supabase_key)

@team_router.post("/teams")
def create_team(name: str,email:str,role:str,hourly_rate:float):
    new_team = {
        "id": str(uuid4()),
        "name": name,
        "email":email,
        "role":role,
        'hourly_rate':hourly_rate

    }
    result = db.table("task_management_team_members_users").insert(new_team).execute()
    return {
        "message": "Team created.",
        "team": result.data
    }

@team_router.post("/teams/{team_id}/members")
def add_team_member(name: str, email: str, role: str, hourly_rate: float):
    new_member = {
        "id": str(uuid4()),
        "name": name,
        "email": email,
        "role": role,
        "hourly_rate": hourly_rate
    }
    result = db.table("task_management_team_members_users").insert(new_member).execute()
    return {
        "message": "New member added to the team",
        "member": result.data
    }