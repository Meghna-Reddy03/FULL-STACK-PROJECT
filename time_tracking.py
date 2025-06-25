from fastapi import APIRouter
from supabase import create_client
from uuid import uuid4
from datetime import datetime, timezone

time_router = APIRouter()

supabase_url = "https://eiselzqyfstbfttivvfh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVpc2VsenF5ZnN0YmZ0dGl2dmZoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4MjE4MDUsImV4cCI6MjA2NTM5NzgwNX0.6p75-Ye3zfMI4MilZrP6d2hat7G1PBtEArHHb9Uwupo"

db = create_client(supabase_url, supabase_key)

@time_router.post("/time-entries")
def start_time_tracking(task_id: str, user_name: str, description: str = "", billable: bool = False, hourly_rate: float = 0.0):
    entry_id = str(uuid4())
    current_datetime = datetime.now(timezone.utc).isoformat()

    new_entry = {
        "id": entry_id,
        "task_id": task_id,
        "user_name": user_name,
        "start_time": current_datetime,
        "end_time": None,
        "duration_minutes": None,
        "description": description,
        "billable": billable,
        "hourly_rate": hourly_rate
    }
    result = db.table("task_management_time_tracking").insert(new_entry).execute()
    return {
        'message':'time tracking started',
        'entry_id':entry_id,
        'data':result.data
        }
