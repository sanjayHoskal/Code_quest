# curriculum_builder.py
# Comprehensive procedural generator for Python and Java challenges

def create_order_q(question, blocks, hint1, hint2, explanation):
    return {
        "type": "order",
        "question": question,
        "blocks": [{"id": f"b{i+1}", "text": text} for i, text in enumerate(blocks)],
        "hint1": hint1,
        "hint2": hint2,
        "explanation": explanation
    }

def create_fill_q(question, code_snippet, correct_answer, hint1, hint2, explanation):
    return {
        "type": "fill",
        "question": question,
        "code_snippet": code_snippet,
        "correct_answer": correct_answer,
        "hint1": hint1,
        "hint2": hint2,
        "explanation": explanation
    }

def create_debug_q(question, code_snippet, correct_answer, hint1, hint2, explanation):
    return {
        "type": "debug",
        "question": question,
        "code_snippet": code_snippet,
        "correct_answer": correct_answer,
        "hint1": hint1,
        "hint2": hint2,
        "explanation": explanation
    }

def create_predict_q(question, code_snippet, correct_answer, hint1, hint2, explanation):
    return {
        "type": "predict",
        "question": question,
        "code_snippet": code_snippet,
        "correct_answer": correct_answer,
        "hint1": hint1,
        "hint2": hint2,
        "explanation": explanation
    }

def create_mcq_q(question, code_snippet, options, correct_answer, hint1, hint2, explanation):
    return {
        "type": "mcq",
        "question": question,
        "code_snippet": code_snippet,
        "options": options,
        "correct_answer": correct_answer,
        "hint1": hint1,
        "hint2": hint2,
        "explanation": explanation
    }

def create_bool_q(question, code_snippet, correct_answer, hint1, hint2, explanation):
    return {
        "type": "boolean",
        "question": question,
        "code_snippet": code_snippet,
        "correct_answer": correct_answer,
        "hint1": hint1,
        "hint2": hint2,
        "explanation": explanation
    }

