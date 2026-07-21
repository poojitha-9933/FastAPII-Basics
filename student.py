from fastapi import FastAPI, HTTPException

app = FastAPI()

students = {
    1: {"name": "Poojitha", "course": "CSE"},
    2: {"name": "Rahul", "course": "ECE"},
    3: {"name": "Priya", "course": "IT"}
}

# Get all students
@app.get("/students")
def get_all_students():
    return students

# Get one student by ID
@app.get("/student/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student ID not found")
    return students[student_id]