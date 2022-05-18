def extract_emp_from_req(request, fields):
    emp = {}
    for field in fields:
        if field in request.json:
            emp[field] = request.json[field]
    if "identity" in emp:
        emp["_id"] = emp["identity"]
    return emp
