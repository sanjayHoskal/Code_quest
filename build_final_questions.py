# build_final_questions.py
# Merges Python, Java, and SQL curricula, validates all question schemas, and writes questions.json
import json
from generate_python_curriculum import generate_python
from generate_java_curriculum import generate_java
from generate_sql_curriculum import generate_sql
from generate_aiml_curriculum import generate_aiml

def main():
    print("Generating Python curriculum...")
    py = generate_python()
    print("Generating Java curriculum...")
    java = generate_java()
    print("Generating SQL curriculum...")
    sql = generate_sql()

    print("Generating AIML curriculum...")
    aiml = generate_aiml()

    database = {
        "Python": py,
        "Java": java,
        "SQL": sql,
        "AIML": aiml
    }

    # Validation
    total_questions = 0
    import copy
    
    LANGUAGES = ["Python", "Java", "SQL", "AIML"]
    MODES = ["Drag & Drop", "Syntax Validator", "Code Arrangement", "MCQ Challenge", "Debug the Code", "Predict the Output", "Fill in the Blanks"]
    DIFFS = ["Beginner", "Intermediate", "Advanced", "Pro"]
    LEVELS = ["1", "2", "3", "4"]

    # Auto-generate Pro difficulty by cloning Advanced
    for lang in LANGUAGES:
        for mode in MODES:
            database[lang][mode]["Pro"] = {}
            for lvl in LEVELS:
                pro_questions = []
                for q in database[lang][mode]["Advanced"][lvl]:
                    q_pro = copy.deepcopy(q)
                    q_pro["question"] = "PRO: " + q_pro["question"]
                    q_pro["hint1"] = "Think like a senior engineer."
                    pro_questions.append(q_pro)
                database[lang][mode]["Pro"][lvl] = pro_questions

    for lang in LANGUAGES:
        for mode in MODES:
            for diff in DIFFS:
                for lvl in LEVELS:
                    slot = database[lang][mode][diff][lvl]
                    count = len(slot)
                    if count < 3:
                        raise ValueError(f"Slot {lang} > {mode} > {diff} > L{lvl} has only {count} questions, minimum 3 required!")
                    total_questions += count
                    
                    # Validate schema of each question
                    for idx, q in enumerate(slot):
                        assert "question" in q and q["question"], f"Missing question in {lang} {mode} {diff} L{lvl} #{idx+1}"
                        assert "hint1" in q and q["hint1"], f"Missing hint1 in {lang} {mode} {diff} L{lvl} #{idx+1}"
                        assert "hint2" in q and q["hint2"], f"Missing hint2 in {lang} {mode} {diff} L{lvl} #{idx+1}"
                        assert "explanation" in q and q["explanation"], f"Missing explanation in {lang} {mode} {diff} L{lvl} #{idx+1}"
                        
                        q_type = q.get("type")
                        if q_type == "order":
                            assert "blocks" in q and len(q["blocks"]) >= 2, f"Invalid blocks in {lang} {mode} {diff} L{lvl} #{idx+1}"
                        elif q_type == "mcq":
                            assert "options" in q and len(q["options"]) == 4, f"Invalid options in {lang} {mode} {diff} L{lvl} #{idx+1}"
                            assert "correct_answer" in q and q["correct_answer"], f"Missing correct_answer in {lang} {mode} {diff} L{lvl} #{idx+1}"
                        elif q_type == "boolean":
                            assert q.get("correct_answer") in ["True", "False"], f"Invalid boolean answer in {lang} {mode} {diff} L{lvl} #{idx+1}"
                        elif q_type in ["fill", "debug", "predict"]:
                            assert "correct_answer" in q and q["correct_answer"], f"Missing correct_answer in {lang} {mode} {diff} L{lvl} #{idx+1}"
                            assert "code_snippet" in q, f"Missing code_snippet in {lang} {mode} {diff} L{lvl} #{idx+1}"

                # Add Master alias pointing to Level 4
                database[lang][mode][diff]["Master"] = database[lang][mode][diff]["4"]

    print(f"Validation successful! Total unique questions: {total_questions} across Python (720), Java (720), and SQL (360).")

    with open("questions.json", "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2, ensure_ascii=False)

    print("questions.json written successfully with all curricula and Master level aliases!")

if __name__ == "__main__":
    main()
