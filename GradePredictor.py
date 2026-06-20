from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create Bayesian Network
model = DiscreteBayesianNetwork([
    ('Attendance', 'AssignmentScore'),
    ('Attendance', 'InternalAssessment'),
    ('StudyHours', 'Motivation'),
    ('AssignmentScore', 'FinalGrade'),
    ('InternalAssessment', 'FinalGrade'),
    ('Motivation', 'FinalGrade')
])

# Attendance CPD
cpd_attendance = TabularCPD(
    'Attendance',
    3,
    [[0.3], [0.4], [0.3]],
    state_names={'Attendance': ['Low', 'Medium', 'High']}
)

# Study Hours CPD
cpd_study = TabularCPD(
    'StudyHours',
    3,
    [[0.35], [0.40], [0.25]],
    state_names={'StudyHours': ['Low', 'Medium', 'High']}
)

# Assignment Score CPD
cpd_assignment = TabularCPD(
    'AssignmentScore',
    3,
    [
        [0.6, 0.3, 0.15],
        [0.3, 0.45, 0.35],
        [0.1, 0.25, 0.50]
    ],
    evidence=['Attendance'],
    evidence_card=[3],
    state_names={
        'AssignmentScore': ['Poor', 'Average', 'Good'],
        'Attendance': ['Low', 'Medium', 'High']
    }
)

# Internal Assessment CPD
cpd_internal = TabularCPD(
    'InternalAssessment',
    3,
    [
        [0.55, 0.30, 0.15],
        [0.35, 0.40, 0.30],
        [0.10, 0.30, 0.55]
    ],
    evidence=['Attendance'],
    evidence_card=[3],
    state_names={
        'InternalAssessment': ['Poor', 'Average', 'Good'],
        'Attendance': ['Low', 'Medium', 'High']
    }
)

# Motivation CPD
cpd_motivation = TabularCPD(
    'Motivation',
    3,
    [
        [0.60, 0.30, 0.10],
        [0.30, 0.45, 0.30],
        [0.10, 0.25, 0.60]
    ],
    evidence=['StudyHours'],
    evidence_card=[3],
    state_names={
        'Motivation': ['Low', 'Medium', 'High'],
        'StudyHours': ['Low', 'Medium', 'High']
    }
)

# Final Grade probabilities
final_fail = []
final_pass = []
final_dist = []

for a in range(3):
    for i in range(3):
        for m in range(3):
            score = a + i + m

            if score <= 2:
                final_fail.append(0.7)
                final_pass.append(0.25)
                final_dist.append(0.05)

            elif score <= 4:
                final_fail.append(0.2)
                final_pass.append(0.5)
                final_dist.append(0.3)

            else:
                final_fail.append(0.05)
                final_pass.append(0.25)
                final_dist.append(0.7)

# Final Grade CPD
cpd_final = TabularCPD(
    'FinalGrade',
    3,
    [final_fail, final_pass, final_dist],
    evidence=['AssignmentScore', 'InternalAssessment', 'Motivation'],
    evidence_card=[3, 3, 3],
    state_names={
        'FinalGrade': ['Fail', 'Pass', 'Distinction'],
        'AssignmentScore': ['Poor', 'Average', 'Good'],
        'InternalAssessment': ['Poor', 'Average', 'Good'],
        'Motivation': ['Low', 'Medium', 'High']
    }
)

# Add CPDs to model
model.add_cpds(
    cpd_attendance,
    cpd_study,
    cpd_assignment,
    cpd_internal,
    cpd_motivation,
    cpd_final
)

# Verify model
assert model.check_model()

# Inference engine
infer = VariableElimination(model)


def get_input(name, options):
    print(f"\n{name}:")
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")

    while True:
        choice = input("Select option number: ")

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]

        print("Invalid choice. Try again.")


# User Input
attendance = get_input("Attendance", ['Low', 'Medium', 'High'])
study_hours = get_input("Study Hours", ['Low', 'Medium', 'High'])

# Perform inference
result = infer.query(
    variables=['FinalGrade'],
    evidence={
        'Attendance': attendance,
        'StudyHours': study_hours
    }
)

# Display results
print("\nStudent Performance Prediction\n")

for grade, prob in zip(result.state_names['FinalGrade'], result.values):
    print(f"{grade}: {prob:.2f}")

predicted = result.state_names['FinalGrade'][result.values.argmax()]

print(f"\nPredicted Final Grade: {predicted}")