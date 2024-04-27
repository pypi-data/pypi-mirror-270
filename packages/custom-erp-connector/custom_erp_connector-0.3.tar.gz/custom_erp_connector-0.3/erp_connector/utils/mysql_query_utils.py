from sqlglot import parse


def _generate_join_clause(joins):
    clauses = []
    for join in joins:
        join_table = join["name"]
        join_alias = join["alias"]
        join_conditions = " AND ".join([
            f"{cond['left']['alias']}.{cond['left']['name']} = {cond['right']['alias']}.{cond['right']['name']}"
            for cond in join["on"]
        ])
        clause = f"JOIN {join_table} AS {join_alias} ON {join_conditions}"
        clauses.append(clause)
    return " ".join(clauses)


def _generate_expr(expr):
    if "column" in expr:
        column = f"{expr['column']['alias']}.{expr['column']['name']}"
        operator = expr["operator"]
        value = expr["value"][0]  # Assuming only one value in the list
        return f"{column} {operator} '{value}'"
    elif "booleanOperator" in expr:
        return expr["booleanOperator"]


def _generate_order_by_clause(order_by):
    clauses = [f"{item['column']['alias']}.{item['column']['name']} {item.get('order', 'ASC')}" for item in order_by]
    return "ORDER BY " + ", ".join(clauses) if clauses else ""


def _generate_where_clause(conditions):
    clauses = []
    for cond_metadata in conditions:
        if "listOfExpr" in cond_metadata:
            sublist = [_generate_expr(expr) for expr in cond_metadata["listOfExpr"]]
            clauses.append("(" + " ".join(sublist) + ")")
        elif "expr" in cond_metadata and "column" in cond_metadata["expr"]:
            expr = cond_metadata["expr"]
            clauses.append(_generate_expr(expr))
    return "WHERE " + " AND ".join(clauses) if clauses else ""


def generate_data_query(json_data):
    queries = []
    for entity in json_data:
        select_clause = ", ".join([f"{item['name']}" for item in entity["select"]])
        from_table = entity["fromTable"]["name"]
        join_clause = _generate_join_clause(entity.get("join", []))
        where_clause = _generate_where_clause(entity.get("where", []))
        order_by_clause = _generate_order_by_clause(entity.get("order_by", []))

        # Construct the SQL query string
        sql_query = f"SELECT {select_clause} FROM {from_table} {join_clause} {where_clause} {order_by_clause}"

        # Parse the SQL query string to validate and normalize it
        parsed_query = parse(sql_query)
        queries.append({"tableName": from_table, "query": str(parsed_query)})
    return queries
