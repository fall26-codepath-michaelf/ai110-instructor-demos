# Instructor Prompts

## Prompt 1

**Interface:** Claude Web

```text
Context: a simple course management systems

Objects: course (has a title and a list of students) and Student (has a name and an ID)

Please provide me some UML, I'd like to model the relationship between the two objects above as classes.
```

## Prompt 2

**Interface:** Claude Web

```text
Let's make a few corrections here to the UML:

1. a student can enroll in many courses, not just one.
2. a course should also have an instructor (let's add an instructor class here as well)
```

## Prompt 3

**Interface:** Claude Code

```text
❯ ┌─────────────────────────────┐
  │           Course             │
  ├─────────────────────────────┤
  │ - title: String               │
  │ - students: List<Student>     │
  │ - instructor: Instructor      │
  ├─────────────────────────────┤
  │ + addStudent(s: Student)      │
  │ + removeStudent(s: Student)   │
  │ + getStudents(): List<Student>│
  │ + getInstructor(): Instructor │
  └─────────────────────────────┘
          o│                    │o
     0..* │└────────────────────┘ 1
           │ enrolls          teaches
     0..* │┌────────────────────┐ 0..*
          o│                    │
 ┌─────────────────────────────┐
 │           Student             │
 ├─────────────────────────────┤
 │ - id: String                  │
 │ - name: String                 │
 │ - courses: List<Course>        │
 ├─────────────────────────────┤
 │ + getId(): String              │
 │ + getName(): String            │
 │ + enroll(c: Course)            │
 └─────────────────────────────┘

 ┌─────────────────────────────┐
 │          Instructor           │
 ├─────────────────────────────┤
 │ - id: String                  │
 │ - name: String                 │
 ├─────────────────────────────┤
 │ + getId(): String              │
 │ + getName(): String            │
 └─────────────────────────────┘

I have this UML above here, describing my course management system, can you
please give me the scaffolding to generate classes for this diagram.
```
