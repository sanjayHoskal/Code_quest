from curriculum_builder import create_order_q, create_fill_q, create_debug_q, create_predict_q, create_mcq_q, create_bool_q

def generate_aiml():
    modes = ["Drag & Drop", "Syntax Validator", "Code Arrangement", "MCQ Challenge", "Debug the Code", "Predict the Output", "Fill in the Blanks"]
    diffs = ["Beginner", "Intermediate", "Advanced"]
    levels = ["1", "2", "3", "4"]
    
    aiml = {mode: {diff: {lvl: [] for lvl in levels} for diff in diffs} for mode in modes}
    
    # Fill with generic AI/ML questions
    for mode in modes:
        for diff in diffs:
            for lvl in levels:
                questions = []
                for i in range(3):
                    if mode in ["Drag & Drop", "Code Arrangement"]:
                        questions.append(create_order_q(f"Arrange the code to train a model ({diff} L{lvl} #{i+1})", ["import pandas as pd", "model = LinearRegression()", "model.fit(X, y)"], "Import libraries.", "Initialize model.", "Fit the model."))
                    elif mode == "Fill in the Blanks":
                        questions.append(create_fill_q(f"Fill in the blank to predict ({diff} L{lvl} #{i+1})", "predictions = model._______(X_test)", "predict", "Use predict method.", "Look at docs.", "It generates predictions."))
                    elif mode == "Debug the Code":
                        questions.append(create_debug_q(f"Fix the shape error ({diff} L{lvl} #{i+1})", "X = X.reshape(-1)", "X = X.reshape(-1, 1)", "Data needs 2D shape.", "Look at reshape.", "Scikit-learn expects 2D arrays."))
                    elif mode == "Predict the Output":
                        questions.append(create_predict_q(f"Predict the output shape ({diff} L{lvl} #{i+1})", "print(np.array([1, 2, 3]).shape)", "(3,)", "It's a 1D array.", "Check numpy docs.", "Tuple with one element."))
                    elif mode == "MCQ Challenge":
                        questions.append(create_mcq_q(f"What does ReLU do? ({diff} L{lvl} #{i+1})", "def relu(x):\n  return max(0, x)", ["It outputs max(0, x)", "It outputs min(0, x)", "It normalizes data", "It calculates loss"], "It outputs max(0, x)", "Think about activation.", "What happens to negative numbers?", "It zeroes out negative values."))
                    elif mode == "Syntax Validator":
                        questions.append(create_bool_q(f"Is this a valid Keras layer? ({diff} L{lvl} #{i+1})", "Dense(64, activation='relu')", "True" if i%2==0 else "False", "Check keras docs.", "Dense is standard.", "It is a valid layer."))
                aiml[mode][diff][lvl] = questions
    return aiml
