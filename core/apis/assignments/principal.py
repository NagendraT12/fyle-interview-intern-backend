from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from flask import make_response, jsonify
from .schema import AssignmentSchema, AssignmentSubmitSchema, AssignmentGradeSchema

principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)
 
@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """List all submitted and graded assignments"""
    print('i')
    assignments = Assignment.get_graded_submitted_assignment() 
    print(assignments)
    assignments_dump = AssignmentSchema().dump(assignments, many=True)
    return APIResponse.respond(data=assignments_dump)

@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    assignment = Assignment.query.get(grade_assignment_payload.id)
    
    if not assignment:
        error_response = {
            'error': 'FyleError',
            'message': 'assignment not found'
        }
        return make_response(jsonify(error_response), 404)
    if assignment.state == 'DRAFT':
        error_response = {
            'error': 'FyleError',
            'message': 'this assignment cant be graded'
        }
        return make_response(jsonify(error_response), 400)
    print(assignment.state)
    graded_assignment = Assignment.mark_grade(
        _id=assignment.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()

    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
