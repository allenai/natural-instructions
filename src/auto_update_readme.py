import json
from os import listdir, path
from os.path import isfile, join

"""
For each updated task file, automatically update its corresponding line in README with new Category, Domain, Input Language and Output Language
"""

def add_to_list(l, index, value):
    if len(l) < index+1:
        l.append(value)
    else: 
        l[index] = value

def modify_task_line(task_name, lines, new_fields): 
    for i, line in enumerate(lines):
        fields = [ x.strip() for x in line.split("|")]
        # found the line
        if fields[0] == f"`{task_name}`":
            # modify the feilds
            fields[2] = new_fields["category"]
            add_to_list(fields, 3, new_fields["domains"])
            add_to_list(fields, 4, new_fields["input_language"])
            add_to_list(fields, 5, new_fields["output_language"])

            lines[i] = "\t| ".join(fields) + "\n"

# write
def update_readme(readme_path, lines):
    out = open(readme_path, 'w')
    out.writelines(lines); out.close()


if __name__ == "__main__":
    tasks_path = 'tasks/'
    readme_path = f"{tasks_path}README.md"

    lines = open(readme_path, 'r').readlines()

    files = [f for f in listdir(tasks_path) if isfile(join(tasks_path, f))]
    files.sort()

    for file in files:
        if ".json" in file:
            file_path = tasks_path + file
            # open each json file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "Domains" in data and "Input_language" in data and "Output_language" in data: 
                    task_name = path.splitext(file)[0]
                    new_fields = {
                        "category": ", ".join(data["Categories"]),
                        "domains": ", ".join(data["Domains"]),
                        "input_language": ", ".join(data["Input_language"]),
                        "output_language": ", ".join(data["Output_language"])
                    }
                    modify_task_line(task_name, lines, new_fields)
                    update_readme(readme_path, lines)
                    print(f"Updated task {task_name} in readme")