def decompose_questions_to_steps(question: str) -> List[str]:
    """Break down a question into the basic steps required to answer it.\n A question decomposition is a numbered list of operations that must be performed to answer the original question. Imagine explaining your question to a friendly droid by listing each action it should take in order for the question to be answered. Each step in our decomposition should refer to either an entity (known or unknown), a propery of an entity or a query operation (count, group, union, etc.)\n Here are the list of step templates and their description:\n Select: A select step is used to return a set of objects. There are no references to previous steps in a select step. template: Return [attributes]\n Filter: A filter step is used to return results from a previous step to which a certain condition applies. template: Return [#step] [condition]\n Project: A project step should return certain attributes of the results of a previous step. template: Return [attributes] of [#step]\n Aggregate: An aggregate step returns an aggregator function applied on a step's result. template: Return the [aggregator] of [#step].\n Group: A group step is an aggregator applied on attributes. template: Return the [aggregator] of [#step] for each [attribute]\n Superlative: A superlative step is used to return the result with a highest/lowest attribute among other results. template: Return [#step1] [where] [#step2] [is] [highest / lowest]\n Comparative: A comparative step is used when we need to compare an attribute with a number to filter results. template: Return [#step1] [where] [#step2] [comparator] [number] \n Union: A union step is used to return results of two steps together. template: Return [#step1] [or / ,] [#step2]\n Intersection: An intersection step returns the result that two steps have in common. template: Return [attribute] of both [#step1] and [#step2]\n Discard: A discard step returns result of a step and excludes result of another step from it. template: Return [#step1] besides [#step2]\n Sort: A sort returns result of another step in a specific order. template: Return [#step1] [ordered / sorted by] [#step2]\n Is true: An is true step checks a condition on another result and returns a true or false. template: Return [is / if] [condition]\n Arithmetic: An arithmatic step operates an arithmatic operation on one or more steps. template: Return the [arithmetic op.] of [#step1] [and] [#step2].

    Parameters:
        question: to be broken down into basic steps for answering

    Returns:
        str: list of steps required to answer the question
    """

    # A select step is used to return a set of objects. There are no references to previous steps in a select step.
    select_template = "Return $attributes"

    # A filter step is used to return results from a previous step to which a certain condition applies.
    filter_template = "Return $step_no $condition"

    # A project step should return certain attributes of the results of a previous step.
    project_template = "Return $attributes of $step_no"

    # An aggregate step returns an aggregator function applied on a step's result
    aggregate_template = "Return the $aggregator of $step_no for each $attribute"

    # A superlative step is used to return the result with a highest/lowest attribute among other results.
    superlative_template = "Return $first_step where $second_step is {highest,lowest}"

    # Comparative: A comparative step is used when we need to compare an attribute with a number to filter results.
    comparative_template = "Return $step_2 $comparator $number"

    # Union: A union step is used to return results of two steps together.
    union_template = "Return $step_1 or $step_2"

    # Intersection: An intersection step returns the result that two steps have in common.
    intersection_template = "Return $attribute of both $step_1 and $step_2"

    # Discard: A discard step returns result of a step and excludes result of another step from it.
    discard_template = "Return $step_1 besides $step_2"

    # Sort: A sort returns result of another step in a specific order.
    sort_template = "Return $step_1 ordered by $step2"

    # Is true: An is true step checks a condition on another result and returns a true or false.
    is_true_template = "Return if $condition]"

    # Arithmetic: An arithmatic step operates an arithmatic operation on one or more steps.
    arithmetic_template = "Return the {+,-,/,*} of $step_1 and $step_2."

    # List of supportted steps and their templates
    step_types = {
        "select": "select_template",
        "filter": filter_template,
        "project": project_template,
        "aggregate": aggregate_template,
        "superlative": superlative_template,
        "comparative": comparative_template,
        "union": union_template,
        "intersection": intersection_template,
        "discard": discard_template,
        "sort": sort_template,
        "is_true": is_true_template,
        "arithmatic": arithmetic_template,
    }

    # List each action it should take in order for the question to be answered. Each step in the decomposition should refer to either an entity (known or unknown), a propery of an entity or a query operation (count, group, union, etc.)
    list_of_steps = generate_steps_needed_to_answer_question(question, step_types)

    return list_of_steps


# program
{
    "method": "decompose_questions_to_steps",
    "arguments": {"question": "str"},
    "return": "List[str]",
    "execute": "decompose_questions_to_steps(question)",
}

# preprocessor
def preprocess(input: str):
    question = input.split("question:")[1].strip()
    return question
